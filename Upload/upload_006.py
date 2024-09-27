# step 3: Upload Images to API Endpoint
!pip install requests==2.31.0
!pip install pydicom==2.3.0

import pydicom
import requests

image_path = "https://github.com/deyritwika/Vet_Cloud_Exercise/blob/main/DICOM%20IMAGES/6d4855a4-67af-4dab-b439-f8ac5ff931ff.dcm"
ds = pydicom.dcmread("https://github.com/deyritwika/Vet_Cloud_Exercise/blob/main/DICOM%20IMAGES/6d4855a4-67af-4dab-b439-f8ac5ff931ff.dcm")
 
url = 'https://d2gveozzsod0j7.cloudfront.net/instances/'

headers = {
    "authorization": "Basic YWRtaW46WVpjdz1icHlGMChQN2FURQ==",
}

with open(image_path, 'rb') as file:
    response = requests.post(url, headers=headers, data=file, timeout=3600)

if response.status_code == 200:
    print('successful!')
else:
    print('failed:', response.status_code, response.text)
