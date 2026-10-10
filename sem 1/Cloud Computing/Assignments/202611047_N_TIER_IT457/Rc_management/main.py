import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from presentation.api import router

app = FastAPI(title="Library Management API")

# Add the API routes
app.include_router(router)

# Serve the HTML folder
app.mount("/static", StaticFiles(directory="presentation/static"), name="static")

@app.get("/")
def home_page():
    return FileResponse("presentation/static/index.html")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
