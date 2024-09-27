#step 1: Fetching Metadata (Make request to a Rest API to get info using HTTPS)

# This library is used for making https requests
import requests

# Function created
def fetch_meta_data( sample_id,priority):
    url= "https://87b5hljc7c.execute-api.us-east-2.amazonaws.com/default/sample_metadata"
    headers= {
        "api_key": "qpHEnol5U86TyvQbtfaJn5CzNR6m6jB62dKfYEWw",
        "content_type": "application/json"
}
    api_type= "REST"

    payload= {
        "sample_id": sample_id,
        "priority": priority
}

# Making a POST Request
    response = requests.post(url, headers=headers, json=payload)

# Check if https request is successful

    if response.status_code == 200:
       metadata = response.json()
       print(metadata)
    else:
       print("Error")
