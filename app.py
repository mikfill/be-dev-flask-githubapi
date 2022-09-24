from flask import Flask, request
import requests


app = Flask(__name__)
GIT_TOKEN = 'your token'


@app.route("/<username>/repos", methods=['GET'])
def get_git_repos(username):
    repolist = []
    url = f"https://api.github.com/users/{username}/repos"   
    repos_request = requests.get(url)

    if repos_request.status_code == 200:
        repos_raw_data = repos_request.json()
        for repo in repos_raw_data:
            repolist.append(repo["name"])
        return {'repos': repolist}
    if repos_request.status_code == 404:
        return {'error': 'User not found'}
    if repos_request.status_code == 403:
        return {'error': 'API rate limit exceeded for your ip'}


@app.route("/<username>/<reponame>/issue", methods=['POST'])
def post_git_issue(username, reponame):
    url = f"https://api.github.com/repos/{username}/{reponame}/issues"

    issue_headers = {
         'Authorization': f'Bearer {GIT_TOKEN}',
         'Accept': 'application/vnd.github+json'
    }

    issue_data = request.json
    response = requests.post(url, json=issue_data, headers=issue_headers)

    if response.status_code == 201:
        return {'issue_created': True}
    else:
        return {'issue_created': False}


