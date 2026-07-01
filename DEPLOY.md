# Deploying NexYouth

The public site is a Flask app that gets **frozen** into plain static HTML and
served by **Cloudflare Pages**. You never edit the live site directly — you edit
here, push to GitHub, and Cloudflare rebuilds and publishes automatically.

## The three roles
- **Registrar** (Network Solutions) — owns the domain `nexyouth.org`, points it at the host.
- **Code source** (GitHub `NexYouth/nexyouth`) — stores the code, triggers deploys.
- **Host** (Cloudflare Pages) — runs the build and serves the site to visitors.

## How a deploy works
1. You edit files locally (`templates/`, `static/`, `app.py`).
2. `freeze.py` renders every public page to `dist/` and copies static assets.
3. On every push to `main`, Cloudflare runs that build and serves `dist/`.

## To update the live site
```bash
# 1. (optional) preview locally
python3 app.py            # → http://localhost:8000

# 2. ship it
git add -A
git commit -m "what changed"
git push origin main      # Cloudflare auto-builds + publishes in ~1–2 min
```

## Cloudflare Pages build settings (set once, in the dashboard)
Workers & Pages → **nexyouth** → Settings → Build:
- **Framework preset:** None
- **Build command:** `pip install -r requirements.txt && python freeze.py`
- **Build output directory:** `dist`
- **Environment variable:** `PYTHON_VERSION` = `3.12` (so the build image uses Python)

## Good to know
- `dist/` is generated, never committed (see `.gitignore`).
- Files over 25 MB are skipped automatically — that's Cloudflare's per-file cap; `freeze.py` handles it.
- All public forms are external **JotForm** / **Zeffy** embeds, so they work fine on a static site.
- The eco-classroom LMS (registration, admin, PDF certs) is dynamic and is **not**
  part of the static site. If it's ever switched on, it needs its own small service.
