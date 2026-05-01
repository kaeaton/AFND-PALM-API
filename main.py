from fastapi import FastAPI
from fastapi.responses import FileResponse
import subprocess
from pathlib import Path
import rpy2.robjects as ro
from rpy2.robjects.packages import importr
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.get("/palm")
async def palm(allele: str):

    # Allows rpy2 to find its config settings even in a thread
    with ro.default_converter.context():

        # Load SSHAARP and the Solberg dataset
        sshaarp = importr('SSHAARP')
        solberg_dataset = ro.r("SSHAARP::solberg_dataset")

        # Generate the image
        sshaarp.PALM(allele, variantType="allele", filename=solberg_dataset, resolution = 500)

        # filename = allele.replace(':', '/') + '.jpg'
        filename = allele + '.jpg'
        file = Path(".", filename)

        return FileResponse(file)