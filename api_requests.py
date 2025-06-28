import requests

def get_posts(page):

    url = f'http://gutendex.com/books/?page={page}&sort='

    print("loading...")
    try:
        response = requests.get(url)

        if response.status_code == 200: #successful
            posts = response.json()
            return posts
        else:
            print('Error', response.status_code)
            return None
    except requests.exceptions.RequestException as e:
        print('Error:',e)
        return None

def get_next_page(next):
    
    url = next

    print("loading...")
    try:
        response = requests.get(url)

        if response.status_code == 200: #successful
            posts = response.json()
            return posts
        else:
            print('Error', response.status_code)
            return None
    except requests.exceptions.RequestException as e:
        print('Error:',e)
        return None