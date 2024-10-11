import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get GitHub token from environment variables
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')

# Check if the token is loaded
if GITHUB_TOKEN is None:
    print("Error: GITHUB_TOKEN not found. Please check your .env file.")
    exit()

# Set headers for authentication
headers = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

# Define the API URL to search for Python files related to web scraping
search_query = "web+scraping+extension:py+in:file"
api_url = f"https://api.github.com/search/code?q={search_query}"

# Make the API request
response = requests.get(api_url, headers=headers)

# Check the response status code
if response.status_code == 200:
    data = response.json()
    # Print out the first few results
    print("Search Results:")
    for item in data.get('items', []):
        print(f"Repository: {item['repository']['full_name']}")
        print(f"File: {item['name']}")
        print(f"URL: {item['html_url']}")
        print("----")
else:
    print(f"Error: {response.status_code} - {response.reason}")
    if response.status_code == 401:
        print("Unauthorized. Please check your GitHub token.")

# Exit the script
exit()
