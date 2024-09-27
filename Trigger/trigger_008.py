!pip install requests==2.31.0
!pip install pydicom==2.3.0

import pydicom
import requests

image_path = "https://github.com/deyritwika/Vet_Cloud_Exercise/blob/main/DICOM%20IMAGES/e644c339-6b50-435e-a1f5-2cc2e01459b0%20(1).dcm"
ds = pydicom.dcmread("https://github.com/deyritwika/Vet_Cloud_Exercise/blob/main/DICOM%20IMAGES/e644c339-6b50-435e-a1f5-2cc2e01459b0%20(1).dcm")

url = "https://zz59wxzzz1.execute-api.us-east-2.amazonaws.com/default/sample_analytics"
api_key = "q7aokbLl8n5jl7O0eOiGg3ddxdivkzKy48gpQZiX"

def trigger_analytics(sample_id, request_type):
  headers = {
      "api_key": api_key,
      "Content-Type": "application/json" 
  }
  payload = {
      "sample_id": sample_id,
      "request_type":request_type 
  }

  response = requests.post(url, headers=headers, json=payload)
  if response.status_code == 200:
      print("Analytics data sent successfully!")
  else:
      print(f"Error sending analytics data: {response.status_code}, {response.text}")
