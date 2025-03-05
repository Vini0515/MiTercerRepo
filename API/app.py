import os
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/familia")
def get_familia():
    rows = ["Vini", "Lu",]
    return rows

@app.get("/superheroesDC")
def get_superheroes():
    rows = ["Superman", "Batman", "Flash", "Linterna Verde", "Mujer maravilla", "Aquaman", "Shazam", "Cyborg"]
    return rows


@app.get("/cursos PLATZI")
def get_CURSOS():
    rows = ["Docker", "Bash", "Linux", "Python", "JavaScrpt", "GitHub", "SCRUM"]
    return rows    