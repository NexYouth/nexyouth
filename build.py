"""
Build the NexYouth static site: render the Jinja templates in templates/ to
plain HTML in dist/, and copy the static assets alongside.

No server, no framework — the site is static content served by Cloudflare Pages.

    python3 build.py    ->  dist/
"""
import os
import shutil

from jinja2 import Environment, FileSystemLoader, select_autoescape

HERE = os.path.dirname(os.path.abspath(__file__))
DIST = os.path.join(HERE, "dist")

# Cloudflare Pages rejects any single file larger than this.
CF_MAX_BYTES = 25 * 1024 * 1024

# Output path (as served) -> template file.
PAGES = {
    "index.html": "home.html",
    "about.html": "about.html",
    "contact.html": "contact.html",
    "partner.html": "partner.html",
    "partnership-packages.html": "partnership-packages.html",
    "success.html": "success.html",
    "programs/skill-development.html": "skill-development.html",
    "programs/debate.html": "debate.html",
    "programs/seminars.html": "seminars.html",
    "programs/mentorship.html": "mentorship.html",
    "programs/environmental-competition.html": "environmental-competition.html",
    "programs/iyec-2026-results.html": "iyec-2026-results.html",
    "programs/youth-tech-lab.html": "youth-tech-lab.html",
    "programs/eco-classroom.html": "eco-classroom.html",
    "programs/eco-classroom/eco-literacy.html": "course-eco-literacy.html",
    "404.html": "404.html",
}

env = Environment(
    loader=FileSystemLoader(os.path.join(HERE, "templates")),
    autoescape=select_autoescape(["html", "xml"]),
)


def _skip_oversized(dirpath, names):
    """copytree filter: drop files over Cloudflare's per-file cap."""
    skip = []
    for name in names:
        full = os.path.join(dirpath, name)
        if os.path.isfile(full) and os.path.getsize(full) > CF_MAX_BYTES:
            skip.append(name)
            mb = os.path.getsize(full) // 1024 // 1024
            print(f"  skip {os.path.relpath(full, HERE)} ({mb}MB > 25MB Cloudflare cap)")
    return skip


def main():
    shutil.rmtree(DIST, ignore_errors=True)
    os.makedirs(DIST)

    for out_path, template in PAGES.items():
        html = env.get_template(template).render()
        dest = os.path.join(DIST, out_path)
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        with open(dest, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"  {out_path}")

    shutil.copytree(
        os.path.join(HERE, "static"),
        os.path.join(DIST, "static"),
        ignore=_skip_oversized,
    )
    print(f"\n{len(PAGES)} pages built -> dist/")


if __name__ == "__main__":
    main()
