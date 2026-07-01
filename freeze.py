"""
Freeze the public marketing site to static HTML for Cloudflare Pages.

The public site has no real backend: content pages are plain template renders,
and every form is an external JotForm / Zeffy embed. So we render each public
route once through Flask's test client and write it to dist/ as static HTML,
then copy static/ alongside. The eco-classroom LMS API/admin (the only genuinely
dynamic surface) is intentionally NOT frozen — it needs a server if ever enabled.

Run:  python3 freeze.py   ->  produces dist/  (deploy that folder)
"""
import os
import shutil

from app import app

# Public GET routes that render static content (no per-request data).
ROUTES = [
    "/",
    "/about",
    "/contact",
    "/partner",
    "/partnership-packages",
    "/success",
    "/programs/environmental-competition",
    "/programs/iyec-2026-results",
    "/programs/eco-classroom",
    "/programs/eco-classroom/eco-literacy",
    "/programs/mentorship",
    "/programs/seminars",
    "/programs/skill-development",
    "/programs/youth-tech-lab",
]

DIST = os.path.join(os.path.dirname(__file__), "dist")

# Cloudflare Pages rejects any single file larger than this.
CF_MAX_BYTES = 25 * 1024 * 1024


def _skip_oversized(dirpath, names):
    """copytree ignore-callback: drop files over Cloudflare's per-file cap."""
    skip = []
    for n in names:
        full = os.path.join(dirpath, n)
        if os.path.isfile(full) and os.path.getsize(full) > CF_MAX_BYTES:
            skip.append(n)
            mb = os.path.getsize(full) / 1024 / 1024
            print(f"  SKIP {os.path.relpath(full)} ({mb:.0f}MB > 25MB Cloudflare limit)")
    return skip


def route_to_path(route):
    """/ -> dist/index.html ; /about -> dist/about.html ; nested keeps folders."""
    if route == "/":
        return os.path.join(DIST, "index.html")
    return os.path.join(DIST, route.lstrip("/") + ".html")


def main():
    shutil.rmtree(DIST, ignore_errors=True)
    os.makedirs(DIST)

    client = app.test_client()
    for route in ROUTES:
        resp = client.get(route)
        assert resp.status_code == 200, f"{route} -> {resp.status_code} (expected 200)"
        path = route_to_path(route)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "wb") as f:
            f.write(resp.data)
        print(f"  froze {route}  ->  {os.path.relpath(path, DIST)}")

    # Cloudflare Pages serves /404.html for unmatched routes.
    resp = client.get("/__no_such_page__")
    with open(os.path.join(DIST, "404.html"), "wb") as f:
        f.write(resp.data)
    print("  froze 404 page")

    shutil.copytree(
        os.path.join(os.path.dirname(__file__), "static"),
        os.path.join(DIST, "static"),
        ignore=_skip_oversized,
    )
    print("  copied static/")
    print(f"\nDone. Deploy the '{os.path.basename(DIST)}/' folder to Cloudflare Pages.")


if __name__ == "__main__":
    main()
