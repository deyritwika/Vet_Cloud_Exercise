# Blood Smear Microscopy Image Processing

## Goal
Fetch metadata for a set of blood smear microscopy images, add the metadata to the images as DICOM tags, upload the images to an imaging server, and trigger analytics once the image upload is complete.

## Steps

### 1. Fetch Metadata
- Use the provided API endpoint to retrieve metadata for a sample set of blood smear microscopy images.

### 2. Prepare DICOM Images
- Load the provided blood smear images as DICOM files.
- Add the fetched metadata to the DICOM tags of each image using appropriate DICOM data elements.
- Ensure that the metadata is added accurately and consistently across all the images.

### 3. Upload Images to Imaging Server
- Use the provided API endpoint to upload the modified DICOM images to the imaging server.
- Verify that the images are uploaded successfully.

### 4. Trigger Analytics
- Use the provided API endpoint to trigger analytics once the images have been successfully uploaded.

## API Information

### Metadata Endpoint
- **URL**: `https://87b5hljc7c.execute-api.us-east-2.amazonaws.com/default/sample_metadata`
- **API Key**: `qpHEnol5U86TyvQbtfaJn5CzNR6m6jB62dKfYEWw`
- **API Type**: REST
- **Method**: ANY
- **Payload**: 
  ```json
  {
      "sample_id": "str",
      "priority": "int"
  }
### Image Upload Endpoint
- **URL**: `https://87b5hljc7c.execute-api.us-east-2.amazonaws.com/default/sample_metadata](https://d2gveozzsod0j7.cloudfront.net/instances/`
- **Authorization**: `Basic YWRtaW46WVpjdz1icHlGMChQN2FURQ==`
- **API Type**: REST
- **Method**: POST
- **Payload**: 
  ```json
  {
      "data": "byte",
      "timeout": "3600"
  }
### Analytics Endpoint
- **URL**: `https://zz59wxzzz1.execute-api.us-east-2.amazonaws.com/default/sample_analytics`
- **API Key**: `q7aokbLl8n5jl7O0eOiGg3ddxdivkzKy48gpQZiX`
- **API Type**: REST
- **Method**: ANY
- **Payload**: 
  ```json
  {
      "sample_id": "str",
      "request_type": "metadata.test_type"
  }
