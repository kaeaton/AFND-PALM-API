from fastapi import FastAPI
import subprocess
***REMOVED***

import rpy2.robjects as ro
from rpy2.robjects.packages import importr
app = FastAPI(***REMOVED***


@app.get("/"***REMOVED***
async def root(***REMOVED***:
    return {"message": "Hello World"}


@app.get("/hello/{name}"***REMOVED***
async def say_hello(name: str***REMOVED***:
    return {"message": f"Hello {name}"}

@app.get("/palm"***REMOVED***
async def palm(allele: str***REMOVED***:

     with ro.default_converter.context(***REMOVED***:
        sshaarp = importr('SSHAARP'***REMOVED***
        solberg_dataset = ro.r("SSHAARP::solberg_dataset"***REMOVED***
    # palm = importr('PALM'***REMOVED***

        image = sshaarp.PALM(allele, variantType="allele", filename=solberg_dataset, resolution = 500***REMOVED***
    # Define the command to run the R script
    # command = 'Rscript'
    # path_to_script = 'R_pkgs/SSHAARP-AFND/SSHARP_functions_script.R::PALM("DRB1*01:01", variantType="allele", color=F, mask = T, filename=SSHAARP::solberg_dataset, resolution = 480***REMOVED***'
    #
    # # Optional: Add command-line arguments to pass to R
    # args = 'PALM("DRB1*01:01", variantType="allele", mask = T, filename=SSHAARP::solberg_dataset, resolution = 500***REMOVED***'
    #
    # # Build and execute the command
    # cmd = [command, path_to_script] #+ args
    # result = subprocess.check_output(cmd, universal_newlines=True***REMOVED***
    #
    # # PALM("DRB1*01:01", variantType="allele", color=F, mask = T, filename=SSHAARP::solberg_dataset, resolution = 480***REMOVED***

        print(image***REMOVED***
        filename = allele.replace(':', '/'***REMOVED***
        file = Path(".", filename***REMOVED***
        return {"image": file}