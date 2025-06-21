from fastapi import FastAPI
from routes import image_generate
import providers

app = FastAPI(
    title="Storyboarder API"
)

@app.on_event("startup")
async def startup_event():
    print("Starting up...")

app.include_router(image_generate.router)

