from httpx import AsyncClient

port = 45302

client = AsyncClient(base_url=f"http://localhost:{port}")
