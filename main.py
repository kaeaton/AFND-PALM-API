from fastapi import FastAPI
from fastapi.responses import FileResponse
import subprocess
from pathlib import Path
from dotenv import load_dotenv
import os
import rpy2.robjects as ro
from rpy2.robjects.packages import importr
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy import text
import pandas as pd

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.get("/palm")
async def palm(allele: str):
    load_dotenv()
    database_password = os.getenv("DB_PASSWORD")

    connection_url = URL.create(
               "mssql+pyodbc",
               username="steve",
               password=database_password, # Special characters are automatically escaped
               host="74.208.198.44",
               port=1433,
               database="allel002",
               query={"driver": "ODBC Driver 18 for SQL Server", "TrustServerCertificate": "yes"}
               )

    engine = create_engine(connection_url)

    # Check image_list.tsv
    image_list = Path("./image_list.tsv")



    # Allows rpy2 to find its config settings even in a thread
    with ro.default_converter.context():

        # Load SSHAARP and the Solberg dataset
        sshaarp = importr('SSHAARP')
        print("imported sshaarp")
        solberg_dataset = ro.r("SSHAARP::solberg_dataset")
        print("found the solberg dataset")

        # Generate the image
        sshaarp.PALM(allele, variantType="allele", filename=solberg_dataset, resolution = 500)

        # filename = allele.replace(':', '/' + '.jpg'
        filename = allele + '.jpg'
        file = Path(".", filename)

        return FileResponse(file)