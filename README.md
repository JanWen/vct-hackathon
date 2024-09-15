# vct-hackathon


# Runnning backend locally

Preparation:
1. Install Python 3 & AWS CLI
2. `cd vct-backend`
3. Create virtual environment (folder where all python deps are installed)  
    `python -m venv .chalice/venv`
4. Activate venv (have to do every time in the terminal when you want to run the server)  
    `.\.chalice\venv\Scripts\Activate.ps1`
5. Install Deps  
    `pip install -r requirements.txt`

Running:
1. make sure you are in vct-backend folder  
    `cd vct-backend`
2. if venv not already active, activate it
    `.\.chalice\venv\Scripts\Activate.ps1`
3. `chalice local --port 8000 --host 0.0.0.0`


# Running frontend locally
Preparation:
1. Install Node.js
2. `cd vct-frontend`
3. Install Deps  
    `npm i`

Running:
1. make sure you are in vct-frontend folder  
    `cd vct-frontend`
2. `npm run dev`


# Text2SQL Infra
1. use aws profile where you want to configure infrastucture  
2. cd infra
3. activate venv `..\vct-backend\.chalice\venv\Scripts\Activate.ps1`
3. python `build_infrastructure.py`  

use `clean.py` to delete all resources!  

## Links

DevPost Resources: https://vcthackathon.devpost.com/resources

Hackathon Technical Docs: https://docs.google.com/document/d/19H3FsWYEli6ShIV5_5fmhq2xDdfcQOCXlRiNvKZLYL8/edit#heading=h.lkyo8c40dcz1

https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html

Hackathon S3 Bucket: https://us-west-2.console.aws.amazon.com/s3/buckets/vcthackathon-data?bucketType=general&region=us-west-2&tab=objects