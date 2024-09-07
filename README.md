# vct-hackathon


# Runnning backend locally

Preparation
1. Install Python 3 & AWS CLI
2. cd vct-backend
3. Create virtual environment (folder where all python deps are installed)
    python -m venv .chalice/venv
4. Activate venv (have to do every time in the terminal when you want to run the server)
    .\.chalice\venv\Scripts\Activate.ps1
5. Install Deps
    pip install -r requirements.txt

Running
1. make sure you are in vct-backend folder
    cd vct-backend
2. if venv not already active, activate it
    .\.chalice\venv\Scripts\Activate.ps1
3. chalice local --port 8000

## Links

DevPost Resources: https://vcthackathon.devpost.com/resources

Hackathon Technical Docs: https://docs.google.com/document/d/19H3FsWYEli6ShIV5_5fmhq2xDdfcQOCXlRiNvKZLYL8/edit#heading=h.lkyo8c40dcz1

https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html

