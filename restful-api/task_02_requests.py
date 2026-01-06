import requests
import csv


def fetch_and_print_posts():
    """Fetches all post from JSONPlaceholder."""
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)
    print("Status code: 200")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post.get('title'))

def fetch_and_save_posts():
    """Fetches all post from JSONPlaceholder and saves it to JSON."""

    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()
        structured_data = []
        for post in posts:
            structured_data.append({
                'id': post.get('id'),
                'title': post.get('title'),
                'body': post.get('body')
            })
        with open('post_pcsv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(structured_data)
