!pip install pydicom==2.3.0

import pydicom
import datetime

def modify_dicom_image(image_path, metadata, sample_id, attempt_num):

    ds= pydicom.dcmread("https://github.com/deyritwika/Vet_Cloud_Exercise/blob/main/DICOM%20IMAGES/661c8904-26b7-48e8-b65c-8028d14069fd.dcm")

    ds.PatientName = metadata.get("PatientName")
    ds.RequestSpecies = metadata.get("RequestSpecies")
    ds.TestType = metadata.get("TestType")
    ds.ClinicName = metadata.get("ClinicName")
    ds.StudyDate = datetime.now().strftime('%Y%m%d')

    ds.save_as("e644c339-6b50-435e-a1f5-2cc2e01459b0.dcm")
    print("DICOM image modified successfully")

    return "e644c339-6b50-435e-a1f5-2cc2e01459b0.dcm"

    sample_id= ' ref0000011tes-cbc-002'
    attempt_num= '005'

    image_path= "https://github.com/deyritwika/Vet_Cloud_Exercise/blob/main/DICOM%20IMAGES/661c8904-26b7-48e8-b65c-8028d14069fd.dcm"

    modified_image_path= modify_dicom_image(image_path, metadata, sample_id, attempt_num)
    print(modified_image_path)
