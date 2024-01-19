import requests

def fetch_api_data(api_url):
    response = requests.get(api_url)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        raise Exception(f"Failed to fetch data from API. Status code: {response.status_code}")