from fastapi import FastAPI
from scraping import Instagram, Tiktok, Youtube, X

app = FastAPI()

@app.get("/instagram/{username}")
def instagram(username: str, type: str = "clean"):
    ig = Instagram()
    return ig.get(f"@{username}", type=type)

@app.get("/tiktok/{username}")
def tiktok(username: str, type: str = "clean"):
    tt = Tiktok()  # <- con minúscula
    return tt.get(f"@{username}", type=type)
