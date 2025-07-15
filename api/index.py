from fastapi import FastAPI
from fastapi.responses import JSONResponse
from mangum import Mangum  # adaptador para serverless

app = FastAPI()

@app.get("/")
def read_root():
    return JSONResponse(content={"message": "API está online!"})

# adaptador para Vercel
handler = Mangum(app)
