from httpx import AsyncClient

port = 45305

client = AsyncClient(base_url=f"http://localhost:{port}")
