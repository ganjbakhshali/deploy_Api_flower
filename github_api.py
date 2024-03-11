import requests

def get_github_user_info(username):
    url = f'https://api.github.com/users/{username}'
    
    try:
        response = requests.get(url)
        response.raise_for_status() 

        user_data = response.json()
        
        followers_count = user_data['followers']
        following_count = user_data['following']
        followers_url = user_data['followers_url']
        
        followers_response = requests.get(followers_url)
        followers_data = followers_response.json()
        follower_names = [follower['login'] for follower in followers_data]
        following_url = user_data['following_url'].split('{')[0]
        following_response = requests.get(following_url)
        following_data = following_response.json()
        following_names = [following['login'] for following in following_data]

        return followers_count, follower_names, following_count, following_names

    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.RequestException as err:
        print(f"Request Exception: {err}")

if __name__ == "__main__":
    github_username = 'ganjbakhshali'

    followers_count, follower_names, following_count, following_names = get_github_user_info(github_username)

    if followers_count is not None and following_count is not None:
        print(f"You have {followers_count} followers:")
        for follower in follower_names:
            print(f"- {follower}")

        print(f"\nYou are following {following_count} users:")
        for following in following_names:
            print(f"- {following}")
    else:
        print("Failed to retrieve GitHub user information.")
