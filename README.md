# Github API with Playwright and Python

The goal of this consume the Github API using Python and Playwright.


## Installation
    $ python -m venv venv
    $ .\venv\Scripts\activate
    $ pip install -r requirements.txt
    $ playwright install chrome

Edit the `config\env.py.template` file and set up your Github credentials
- GITHUB_ACCESS_TOKEN: Github access token
  - Github - Settings - Developer settings - Personal access tokens - Fine-grained tokens
    - Administration - Access: Read and write
    - Issues - Access: Read and write
- GITHUB_USER: Github user name
- GITHUB_REPO: Temporary repository name
Rename the file `config\env.py.template` to `config\env.py`

## Scripts execution
    $ .\venv\Scripts\activate
    $ pytest -v
