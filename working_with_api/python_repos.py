import requests

url = "https://api.github.com/search/repositories"
url += "?q=language:python+stars:>10000&sort=stars"

headers = {"Accept": "application/vnd.github.v3+json"}
#API call, r = API response
r = requests.get(url, headers=headers)
print(f"Status Code: {r.status_code}")

#response body parsing
response_dict = r.json()

print(response_dict.keys())

print(f"total repositories: {response_dict['total_count']}")
print(f"complete results: {not response_dict['incomplete_results']}")

repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

print("\nSelected information about each repository:")
for repo_dict in repo_dicts:
    print(f"Name: {repo_dict["name"]}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Created: {repo_dict['created_at']}")
    print(f"Updated: {repo_dict['updated_at']}")
    print(f"Description: {repo_dict['description']}")

