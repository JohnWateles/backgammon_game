from httpx import AsyncClient

port = 45300

client = AsyncClient(base_url=f"http://localhost:{port}")
