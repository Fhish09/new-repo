from fastapi import FastAPI

app = FastAPI(title="Women Menstruation Aid", description="AI-powered menstrual pain relief companion.")

@app.get("/")
def read_root():
    return {"message": "Welcome to Women Menstruation Aid API"}
