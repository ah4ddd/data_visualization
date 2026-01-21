from operator import itemgetter
import requests

# Get top story IDs
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")

submission_ids = r.json()[:30]  # limit to top 30 so i don’t DDOS myself

submission_dicts = []

for submission_id in submission_ids:
    item_url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(item_url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")

    response_dict = r.json()

    # Defensive coding: some items lack descendants
    submission_dict = {
        'title': response_dict.get('title', 'No title'),
        'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict.get('descendants', 0),
    }

    submission_dicts.append(submission_dict)

# Sort by comment count
submission_dicts = sorted(
    submission_dicts,
    key=itemgetter('comments'),
    reverse=True
)

# Display results
for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")
