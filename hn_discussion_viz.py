from operator import itemgetter
import requests
import plotly.express as px

# 1. Get top story IDs
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")

submission_ids = r.json()[:30]  # limit to top 30

submission_dicts = []

# 2. Fetch details for each story
for submission_id in submission_ids:
    item_url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(item_url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    # Defensive parsing (real-world data is messy)
    title = response_dict.get('title', 'No title')
    comments = response_dict.get('descendants', 0)
    hn_link = f"https://news.ycombinator.com/item?id={submission_id}"

    submission_dict = {
        'title': title,
        'comments': comments,
        'link': hn_link,
    }

    submission_dicts.append(submission_dict)

# 3. Sort by comment count (most active discussions)
submission_dicts = sorted(
    submission_dicts,
    key=itemgetter('comments'),
    reverse=True
)

# 4. Prepare data for visualization
titles = []
comment_counts = []
hover_texts = []

for submission in submission_dicts:
    title = submission['title']
    link = submission['link']
    comments = submission['comments']

    titles.append(f"<a href='{link}'>{title}</a>")
    comment_counts.append(comments)
    hover_texts.append(f"Comments: {comments}")

# 5. Visualize
fig = px.bar(
    x=titles,
    y=comment_counts,
    labels={'x': 'Hacker News Submission', 'y': 'Number of Comments'},
    title='Most Active Hacker News Discussions',
    hover_name=hover_texts
)

fig.update_layout(
    title_font_size=28,
    xaxis_title_font_size=20,
    yaxis_title_font_size=20
)

fig.update_traces(marker_color='crimson', marker_opacity=0.7)

fig.show()
