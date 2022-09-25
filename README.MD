# Be Dev Test FlaskAPI

Simple flask api to interact with github api

## Description

Using this api, you can get a list of the user's public repositories on github and create an issue.

## Getting Started

### Dependencies

* Pyhon 3.8.10
* certifi==2022.9.14
* charset-normalizer==2.1.1
* click==8.1.3
* Flask==2.2.2
* idna==3.4
* importlib-metadata==4.12.0
* itsdangerous==2.1.2
* Jinja2==3.1.2
* MarkupSafe==2.1.1
* requests==2.28.1
* urllib3==1.26.12
* Werkzeug==2.2.2
* zipp==3.8.1

### Installing

* SSH: 
git clone git@github.com:mikfill/be-dev-flask-githubapi.git
* HTTPS: 
git clone https://github.com/mikfill/be-dev-flask-githubapi.git
* Edit variable GIT_TOKEN in app.py 
* pip install -r requirments.txt

### Executing program

```
flask run 
OR RUN WITH DEBUG
flask --debug run
```

## Sample requests

GET list repositories for github user
```c
curl -X GET http://"127.0.0.1:5000/<GIT_USERNAME>/repos"
```
Sample output
```json
{
  "repos": [
    "be-dev-englishbot",
    "be-dev-flask-githubapi",
    "bot-template",
    "Bugs-Hunt-OdynokovTeam",
    "clean-code-javascript",
    "cv-mate-academy",
    "Filippenko_CSharp",
    "git-guide",
    "how-web-works",
    "JavaScript30",
    "reloadium"
  ]
}
```
POST issue to repo
```c
curl -X POST http://127.0.0.1:5000/<GIT_USERNAME>/<GIT_REPONAME>/issue -H 'Content-Type:application/json' -d '{"title":"issue title","body":"test issue text"}'
```
Sample body for POST request from [GitHub Docs](https://docs.github.com/en/rest/issues/issues#create-an-issue)
```json
-d '{
    "title":"Found a bug",
    "body":"I'm having a problem with this.",
    "assignees":["octocat"],
    "milestone":1,
    "labels":["bug"]
    }'
```
Sample output
```json
{
  "issue_created": true
}
```

## Authors

* Discord: [@Mykola Filippenko](https://discordapp.com/users/964209003569766482/)
* Telegram: [@mikfill](https://t.me/mikfill)

## Acknowledgments

* [GitHub Docs](https://docs.github.com/en)
* [Flask Quickstart](https://flask.palletsprojects.com/en/2.2.x/quickstart/)
* [Thunder Client](https://marketplace.visualstudio.com/items?itemName=rangav.vscode-thunder-client)
