from httpx import AsyncClient

port = 45301

client = AsyncClient(base_url=f"http://localhost:{port}")
