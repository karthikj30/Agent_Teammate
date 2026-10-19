"""Vercel entrypoint: the API for the website at https://nirnaya-beyondai.vercel.app (Vercel project nirnaya-api,
root `backend`). The website forwards /api and /mcp here (web/vercel.json). Each instance keeps its own demo
bank in /tmp, so a cold start begins from fresh demo data. Model keys (GROQ_API_KEY and friends) go in the
project's environment variables; without them the agents answer from rules."""
import os

os.environ.setdefault("NIRNAYA_DB", "/tmp/nirnaya/nirnaya.db")
os.environ.setdefault("NIRNAYA_WEB", "/tmp/nirnaya/no-web")  # the website is its own Vercel project
os.makedirs(os.path.dirname(os.environ["NIRNAYA_DB"]), exist_ok=True)

from nirnaya.api import create_app  # noqa: E402  (the env above is read at import)

app = create_app()
