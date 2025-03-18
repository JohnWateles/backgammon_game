from httpx import AsyncClient

port = 45304

client = AsyncClient(base_url=f"http://localhost:{port}")
