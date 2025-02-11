import requests
import json
import pandas as pd
import time
import csv
import os
from url_type import check_url

# Define the API URL
model_url = "http://localhost:11434/api/generate"
input_path = './scraped_domains.csv'
output_path = './output.csv'


categories = ['ALLWebTraffic', 'Activex', 'Advertisements', 'Alcohol & tobacco', 'Anonymizers', 'Applets', 
              'Auctions & classified ads', 'Blogs & forums', 'Business cloud apps', 'Business networking', 
              'CRL and OCSP', 'Command & control', 'Content delivery', 'Controlled substances', 'Cookies', 
              'Criminal activity', 'Download freeware & shareware', 'Dynamic DNS & ISP sites', 'Education', 
              'Entertainment', 'Extreme', 'Fashion & beauty', 'Financial services', 'Gambling', 'Games', 
              'General business', 'Government', 'HTTPUpload', 'Hacking', 'Health & medicines', 'Hobbies', 
              'Hunting & fishing', 'IPAddress', 'Image search', 'Information technology', 'Intellectual piracy', 
              'Intolerance & hate', 'Jobs search', 'Kids', 'Legal highs', 'Live audio', 'Live video', 
              'Marijuana', 'Militancy & extremist', 'Military', 'NGOs & non-profits', 'Newly registered websites', 
              'News', 'None', 'Nudity', 'Online Chat', 'Online shopping', 'Parked Domain', 'Peer-to-peer & torrents', 
              'Personal cloud apps', 'Personal network storage', 'Personal sites', 'Personals & dating', 
              'Phishing & fraud', 'Photo galleries', 'Plagiarism', 'Political organization', 'Portal sites', 
              'Pro-suicide & self-harm', 'Professional & workers organizations', 'Radio & audio hosting', 
              'Reference', 'Religion & spirituality', 'Restaurants & dining', 'Search engines', 'Sex education', 
              'Sexually explicit', 'Social networking', 'Society & culture', 'Software updates', 'Spam URLs', 
              'Sports', 'Spyware & malware', 'Stocks & trading', 'Surveillance', 'Swimwear & lingerie', 
              'Translators', 'Travel', 'Unauthorized software stores', 'Uncategorized', 'Vehicles', 
              'Video hosting', 'Voice & video calls', 'Weapons', 'Web e-mail', 'Geolocation: Web traffic', 'Web Hosting']

def ask_llama(payload):
    with requests.post(model_url, json=payload, stream=True) as response:
        if response.status_code == 200:
            full_response = ""
            for line in response.iter_lines():
                if line:
                    data = json.loads(line.decode('utf-8'))
                    full_response += data.get("response", "")
                    if data.get("done", False):
                        return full_response
            return full_response
        else:
            print(f"Request failed with status code {response.status_code}")
    return None

def generate_payload(content, prompt_type):
    if prompt_type == "category":
        return {
            "model": "llama3.1",
            "prompt": f"{content}, \n\nRead this content carefully. Ignore useless information like cookies and login etc. Tell me what is the most probable category for this website. If it can lie in more than one categories then tell twoo. DO NOT TELL ANY EXPLANATION. JUST TELL THE CATEGORY"
        }
    # elif prompt_type == "sub_category":
    #     return {
    #         "model": "llama3",
    #         "prompt": f"From this list of categories {categories}, choose the options that best fits this {content}. ONLY CHOOSE THE HIGHEST PROBABLE ONE OR TWO, DO NOT WRITE ANYTHING ELSE IN RESPONSE"
    #     }
    return {}

def header_rows(output_path):
    if not os.path.exists(output_path):
        with open(output_path, 'w') as file:
            writer = csv.writer(file)
            writer.writerow(["URL", "Response"])

if __name__ == "__main__":

    now_time = time.time()
    print('starting execition')

    df = pd.read_csv(input_path, nrows=362)
    print('csv file read')
    with open(output_path, 'w', newline='') as file:
        header_rows(output_path)
        writer = csv.writer(file)
        for _, row in df.iterrows():
            url = row["URL"]
            content = row["Content"]
            print(f'processing url {url}' )
            if check_url(url, writer):
                continue

            # Generate the first prompt to determine category
            payload = generate_payload(url+ ' ' +content, "category")
            response = ask_llama(payload)
            
            if response:
                print(f"First response: {response}")

                # Generate the second prompt for sub-category
                # payload = generate_payload(response, "sub_category")
                # category = ask_llama(payload)
                writer.writerow([url, response])

                # if category:
                #     print(f'Final Response: URL: {url} Category: {category}\n')
                # else:
                #     print(f"Error categorizing {url} (sub-category)")
            else:
                print(f"Error categorizing {url} (category)")

    end_time = time.time()


    print(f"Time Taken: {end_time-now_time:.2f}")
