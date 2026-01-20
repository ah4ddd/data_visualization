import requests
import plotly.express as px

url = "https://api.github.com/search/repositories"
url += "?q=language:python+stars:>10000&sort=stars"

headers = {"Accept": "application/vnd.github.v3+json"}
#API call, r = API response
r = requests.get(url, headers=headers)
print(f"Status Code: {r.status_code}")

#response body parsing
response_dict = r.json()
print(f"complete results: {not response_dict['incomplete_results']}")

repo_dicts = response_dict['items']
repo_links, stars, hover_texts = [], [], []
for repo_dict in repo_dicts:
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)
    stars.append(repo_dict['stargazers_count'])

    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    hover_text = f"{owner}<br />{description}"
    hover_texts.append(hover_text)

fig = px.bar(x=repo_links,
             y=stars,
             labels= {'x':'Repository', 'y':'Stars'},
             title='Most-Starred Python Repos on Github',
             hover_name=hover_texts)

fig.update_layout(title_font_size=28,
                  xaxis_title_font_size=20,
                  yaxis_title_font_size=20)

fig.update_traces(marker_color=(255,127,152),
                  marker_opacity=0.6
                  )
fig.show()


