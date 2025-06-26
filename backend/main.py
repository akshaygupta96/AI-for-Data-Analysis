from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from llm_engine import generate_code_from_query
from code_runner import execute_user_code
import pandas as pd
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for dev only
    allow_methods=["*"],
    allow_headers=["*"],
)

dataframe = None  # Global placeholder

@app.post("/upload/")
async def upload_csv(file: UploadFile = File(...)):
    global dataframe
    df = pd.read_csv(file.file)
    dataframe = df
    df.head().to_csv("data/preview.csv", index=False)
    return {"columns": df.columns.tolist(), "rows": df.head(5).to_dict()}

@app.post("/ask/")
async def ask_question(query: str):
    global dataframe
    code = generate_code_from_query(query, dataframe.head())
    result = execute_user_code(code, dataframe)
    return {"code": code, "result": result}
