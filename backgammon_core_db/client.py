from httpx import AsyncClient

port = 45303

client = AsyncClient(base_url=f"http://localhost:{port}")
