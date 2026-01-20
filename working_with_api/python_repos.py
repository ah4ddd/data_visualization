import requests

url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars:>10000"

headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status Code: {r.status_code}")

response_dict = r.json()

print(response_dict.keys())

print(f"total repositories: {response_dict['total_count']}")
print(f"complete results: {not response_dict['incomplete_results']}")

repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

repo_dict = repo_dicts[0]
print(f"\nKeys: {len(repo_dicts)}")
for key in sorted(repo_dict.keys()):
    print(key)
