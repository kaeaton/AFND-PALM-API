import os
from pathlib import Path
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy import text
import pandas as pd



from sqlalchemy import MetaData
import pyodbc
from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy import Table, Column, Integer, String

columns = ['popname', 'contin', 'complex', 'pop_lat1_deg', 'pop_lat1_min', 'pop_lat1_card', 'pop_long1_deg', 'pop_long1_min', 'pop_long1_card', 'locus', 'allele_v2', 'allele_v3', 'allele.freq', 'allele.count', 'gametes']
QUERY = (f"SELECT TOP 2000 \
[dbo].[populat].[pop_name], \
[dbo].[populat].[pop_geog_region], \
[dbo].[populat].[pop_ethnic_origin], \
[dbo].[populat].[pop_lat1_deg], \
[dbo].[populat].[pop_lat1_min], \
[dbo].[populat].[pop_lat1_card], \
[dbo].[populat].[pop_long1_deg], \
[dbo].[populat].[pop_long1_min], \
[dbo].[populat].[pop_long1_card], \
[dbo].[alleles].[all_locus], \
[dbo].[alleles].[all_name2], \
[dbo].[alleles].[all_name], \
[dbo].[allefreq].[allf_gene_freq], \
[dbo].[allefreq].[allf_chrom], \
[dbo].[allefreq].[allf_sample_size] \
FROM [dbo].[populat] \
INNER JOIN [dbo].[allefreq] ON [dbo].[populat].[pop_id] = [dbo].[allefreq].[allf_popid] \
INNER JOIN [dbo].[alleles] ON [dbo].[allefreq].[allf_allele] = [dbo].[alleles].[all_name] \
WHERE [dbo].[populat].[pop_ethnic_origin] != 'Mixed' \
AND [dbo].[allefreq].[allf_polyreg] = 'HLA' \
AND [dbo].[allefreq].[allf_gene_freq] != '0.000'\
AND [dbo].[allefreq].[allf_gene_freq] != '0'\
AND [dbo].[allefreq].[allf_gene_freq] != '' \
AND [dbo].[alleles].[all_locus] = 'DRB1'\
AND [dbo].[alleles].[all_name] = 'DRB1*13:13'")


# load secrets from .env file
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

engine = create_engine(connection_url, echo=True)

with engine.connect() as conn:

    result = conn.execute(text(QUERY))
    df = pd.DataFrame(result, columns=columns)
    # df.apply(lambda x: 2*x, axis=1)
    print(df.iloc[:,[0, 9, 11, 12, 14]])


    # for row in result:
    #     print(row)





