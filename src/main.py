import os
from infra.app import app
import uvicorn
from dotenv import load_dotenv

load_dotenv()
if __name__ == "__main__":
    host = os.getenv("SERVER_HOST") or "127.0.0.1"
    port = os.getenv("SERVER_PORT") or 3000
    print(host, port)
    
    print(f"Servindo em {host}:{port}")
    config = uvicorn.Config("main:app", host=host, port=int(port), log_level="info")
    server = uvicorn.Server(config)
    server.run()
    
    
@app.get('/')
async def read_root():
    return {os.getenv("SERVER_PORT")}