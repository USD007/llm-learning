import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


def get_profile_url_tavily(name: str):
    """Searches for LinkedIn or Twitter Profile Page."""
    # Fetch the API key from environment variables
    api_key = os.getenv("TAVILY_API_KEY")

    if not api_key:
        raise ValueError("API key is missing. Please ensure it is set in the .env file.")

    api_endpoint = 'https://app.tavily.com/playground'
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    params = {'name': name}

    try:
        # Make the GET request to Tavily API
        response = requests.get(api_endpoint, headers=headers, params=params)

        # Check for successful response
        if response.status_code == 200:
            res = response.json()  # Parse the JSON response

            # Check if the result is a list of dictionaries with a 'url' key
            if isinstance(res, list) and len(res) > 0 and 'url' in res[0]:
                return res[0]['url']  # Return the first URL in the search results
            elif isinstance(res, str):
                return res  # If `res` is a string, return it as is
            else:
                raise ValueError("Unexpected response format: No URL found or incorrect response structure")
        elif response.status_code == 401:
            raise PermissionError("Unauthorized: Please check your API key and permissions.")
        else:
            response.raise_for_status()  # Raise an HTTPError for other status codes

    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Request failed: {e}")


# Use the function to get the LinkedIn URL for "ujwal d"
linkedin_url = get_profile_url_tavily("ujwal d")
print("LinkedIn URL:", linkedin_url)
