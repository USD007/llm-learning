from langchain_community.tools import TavilyAnswer
from langchain_community.tools.tavily_search import TavilySearchResults
from dotenv import load_dotenv

load_dotenv()
def get_profile_url_tavily(name: str):
    """Searches for Linkedin or twitter Profile Page."""
    search = TavilySearchResults()  # Initialize the search class
    res = search.run(f"{name}")  # Run the search for the given name

    # Check if the result is a list of dictionaries with a 'url' key
    if isinstance(res, list) and len(res) > 0 and 'url' in res[0]:
        return res[0]['url']  # Return the first URL in the search results

# def get_profile_url_tavily(name: str):
#     return 'https://gist.githubusercontent.com/USD007/9c5fe2f601f933651de64467541c3c5c/raw/47e2b3bd93bbbe68dede8350cd9579a6c5676f51/ujwal-d.json'



# def get_profile_url_tavily(name: str):
#     """Searches for Linkedin or Twitter Profile Page."""
#     url = "https://app.tavily.com/playground"  # Tavily API URL
#     headers = {
#         "Authorization": f"Bearer {TAVILY_API_KEY}",  # Pass the API key in the headers
#         "Content-Type": "application/json"
#     }
#     payload = {
#         "query": name
#     }
#
#     # Make the request to Tavily
#     response = requests.post(url, json=payload, headers=headers)
#
#     try:
#         res = response.json()  # Parse the JSON response
#
#         # Check if the result is a list of dictionaries with a 'url' key
#         if isinstance(res, list) and len(res) > 0 and 'url' in res[0]:
#             return res[0]['url']  # Return the first URL in the search results
#         elif isinstance(res, str):
#             return res  # If `res` is a string, return it as is
#         else:
#             raise ValueError("Unexpected response format: No URL found or incorrect response structure")
#
#     except requests.exceptions.JSONDecodeError:
#         raise RuntimeError(f"Request failed: {response.status_code} {response.text}")


if __name__ == '__main__':
    linkedin_url = get_profile_url_tavily("ujwal d")
    print(linkedin_url)



