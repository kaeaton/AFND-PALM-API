from fastapi import FastAPI
from fastapi.responses import FileResponse
import subprocess
***REMOVED***
***REMOVED***
***REMOVED***
import rpy2.robjects as ro
from rpy2.robjects.packages import importr
***REMOVED***
***REMOVED***
***REMOVED***



app = FastAPI(***REMOVED***


@app.get("/"***REMOVED***
async def root(***REMOVED***:
    return {"message": "Hello World"}


@app.get("/hello/{name}"***REMOVED***
async def say_hello(name: str***REMOVED***:
    return {"message": f"Hello {name}"}

@app.get("/palm"***REMOVED***
async def palm(allele: str***REMOVED***:

    ***REMOVED***
    ***REMOVED***
    ***REMOVED***

    ***REMOVED***
    ***REMOVED***
    ***REMOVED***
    ***REMOVED***
    ***REMOVED***
    ***REMOVED***
    ***REMOVED***
    ***REMOVED***
    ***REMOVED***

    engine = create_engine(connection_url***REMOVED***

    # Check image_list.tsv
    image_list = Path("./image_list.tsv"***REMOVED***



    # Allows rpy2 to find its config settings even in a thread
    with ro.default_converter.context(***REMOVED***:

        # Load SSHAARP and the Solberg dataset
        sshaarp = importr('SSHAARP'***REMOVED***
        print("imported sshaarp"***REMOVED***
        solberg_dataset = ro.r("SSHAARP::solberg_dataset"***REMOVED***
        print("found the solberg dataset"***REMOVED***

        # Generate the image
        sshaarp.PALM(allele, variantType="allele", filename=solberg_dataset, resolution = 500***REMOVED***

        # filename = allele.replace(':', '/'***REMOVED*** + '.jpg'
        filename = allele + '.jpg'
        file = Path(".", filename***REMOVED***

        return FileResponse(file***REMOVED***