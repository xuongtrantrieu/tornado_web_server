from os import getenv as get_env
from dotenv import load_dotenv

load_dotenv()

TOKEN = get_env('GITHUB_TOKEN') or ''
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'token {}'.format(TOKEN)
}

GITHUB_API = 'https://api.github.com'
orgs = ['/twitter/repos', '/auth0/repos', '/nasa/repos', 'mozilla/repos', 'adobe/repos']
