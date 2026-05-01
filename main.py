from fastapi import FastAPI
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

     with ro.default_converter.context():
        sshaarp = importr('SSHAARP')
        solberg_dataset = ro.r("SSHAARP::solberg_dataset")
    # palm = importr('PALM')

        image = sshaarp.PALM(allele, variantType="allele", filename=solberg_dataset, resolution = 500)
    # Define the command to run the R script
    # command = 'Rscript'
    # path_to_script = 'R_pkgs/SSHAARP-AFND/SSHARP_functions_script.R::PALM("DRB1*01:01", variantType="allele", color=F, mask = T, filename=SSHAARP::solberg_dataset, resolution = 480)'
    #
    # # Optional: Add command-line arguments to pass to R
    # args = 'PALM("DRB1*01:01", variantType="allele", mask = T, filename=SSHAARP::solberg_dataset, resolution = 500)'
    #
    # # Build and execute the command
    # cmd = [command, path_to_script] #+ args
    # result = subprocess.check_output(cmd, universal_newlines=True)
    #
    # # PALM("DRB1*01:01", variantType="allele", color=F, mask = T, filename=SSHAARP::solberg_dataset, resolution = 480)

        print(image)
        filename = allele.replace(':', '/')
        file = Path(".", filename)
        return {"image": file}