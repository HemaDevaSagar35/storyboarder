from fastapi import FastAPI
from api.app.routes import image_generate
import providers
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="Storyboarder API"
)

@app.on_event("startup")
async def startup_event():
    print("Starting up...")

app.include_router(image_generate.router)

