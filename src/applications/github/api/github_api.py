import requests


class GitHubAPIClient:
    """Current class contains every API call we use in tests"""

    def __init__(self) -> None:
        pass

    def search_user(self, user_name):
        print("Sending request to url: https://api.github.com/search/users")
        r = requests.get("https://api.github.com/search/users", params={'q': user_name})

        body = r.json()
        print(f"Response retrieved {body}")
        return body

    def search_repos(self, repo_name):
        print("Sending request to url: https://api.github.com/search/repositories")
        r = requests.get("https://api.github.com/search/repositories", params={'q': repo_name})

        body = r.json()
        print(f"Response retrieved {body}")
        return body

    def search_commits(self, commit_hash):
        print("Sending request to url https://api.github.com/search/commits")
        r = requests.get("https://api.github.com/search/commits", params={'q': commit_hash})

        body = r.json()
        print(f"Response retrieved {body}")
        return body
