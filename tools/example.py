"""Example custom tool — uncomment and edit to expose to the agent.

The harness auto-discovers any `@tool`-decorated function in this
directory at boot. Schema is derived from your type hints; the first
docstring line becomes the tool description shown to the model.

See docs/agent-protocols.md for the full contract (supported types,
async tools, error handling, conflict resolution with skill tools).
"""

# from harness.tools import tool
#
#
# @tool(description="Add two integers together.")
# def add(a: int, b: int) -> int:
#     return a + b
#
#
# @tool()
# async def fetch_title(url: str) -> str:
#     """Fetch a URL and return its <title>. Async tools are fine.
#
#     url: where to fetch from.
#     """
#     import httpx
#     async with httpx.AsyncClient() as client:
#         r = await client.get(url, timeout=10)
#     # ... parse title ...
#     return r.text[:80]


# --- Persistence ---------------------------------------------------------
#
# Once your agent picks a Persistence backend in the Runtime tab, Guild
# surfaces the resource name on the agent detail page and grants your
# service account the IAM it needs. You write the SDK calls directly —
# Guild does NOT provide a persistence library (Option A: resource name
# only, agent author owns the SDK + schema + retries).
#
# Firestore (Guild auto-creates the database `agent-{your-slug}` and
# grants the agent SA `roles/datastore.user` scoped to it; no access
# to other agents' or Guild's own data):
#
#   from google.cloud import firestore
#   db = firestore.Client(project="<gcp-project>", database="agent-<slug>")
#
#   @tool(description="Remember a fact about the user.")
#   def remember(key: str, value: str) -> str:
#       db.collection("memory").document(key).set({"value": value})
#       return f"saved {key}"
#
# Cloud SQL Postgres (user-owned: provision the instance, create DB +
# role, store password as a Guild secret, grant roles/cloudsql.client
# to the agent SA, redeploy with --add-cloudsql-instances):
#
#   import os, psycopg
#   conn = psycopg.connect(
#       host=f"/cloudsql/{os.environ['CLOUDSQL_INSTANCE']}",
#       dbname="agent_<slug>", user="agent_<slug>",
#       password=os.environ["DB_PASSWORD"],
#   )
