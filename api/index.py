from fastapi import FastAPI
from apps.calculator.route import router as calculator_router
from constants import SERVER_URL, PORT, ENV
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(calculator_router, prefix="/calculate", tags=["calculate"])

@app.get("/")
async def root():
    return {"message": "Server is running"}
