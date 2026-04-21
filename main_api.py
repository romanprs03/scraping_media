from fastapi import FastAPI
from scraping import Instagram, Tiktok

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok"}

@app.get("/instagram/{username}")
def instagram(username: str, type: str = "clean"):
    ig = Instagram()
    return ig.get(f"@{username}", type=type)

@app.get("/tiktok/{username}")
def tiktok(username: str, type: str = "clean"):
    tt = Tiktok()
    return tt.get(f"@{username}", type=type)
