import os
import requests
from dotenv import load_dotenv

load_dotenv()

def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = False):
    """scraping linked in info """
    if mock:
       #local gist github static file
        linkedin_profile_url = "https://gist.githubusercontent.com/USD007/9c5fe2f601f933651de64467541c3c5c/raw/47e2b3bd93bbbe68dede8350cd9579a6c5676f51/ujwal-d.json"
        response = requests.get(linkedin_profile_url,timeout=10,)
    else:
        #get from scraper
        api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
        header_dic = {"Authorization": f'{os.environ.get("LINKED_IN_API_KEY")}'}
        response = requests.get(api_endpoint,
                                 params={"url": linkedin_profile_url},
                                 headers=header_dic,
                                timeout=10)
    data = response.json()
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
           and k not in ["people_also_viewed", "certifications"]
    }
    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    return data



if __name__ == "__main__":

    print(scrape_linkedin_profile("https://www.linkedin.com/in/ujwal-d-72a66b244/", True))  #takeaway True for realtimedata