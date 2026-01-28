import requests
import os
import uuid


# The complete API endpoint URL for this flow
url = "https://aws-us-east-2.langflow.datastax.com/lf/1ea91116-3aa2-4b30-ab57-4b24606506e6/api/v1/run/bd9b2507-13fb-45bc-9e82-d66943124707"

# Request payload configuration
payload = {
    "output_type": "chat",
    "input_type": "chat",
    "input_value": "hello world!"
}
payload["session_id"] = str(uuid.uuid4())

headers = {
    "X-DataStax-Current-Org": "1208749a-a3b5-449a-b4a5-cf837dd48153", 
    "Authorization": "Bearer AstraCS:hkxkZsIRsiBHzoUoHfUFkSXi:4612af53f436c8bd9ab2f817f538fba228e6c2fed1d580a419c1f5025d6de401",
    "Content-Type": "application/json", 
    "Accept": "application/json",
}

try:
    # Send API request
    response = requests.request("POST", url, json=payload, headers=headers)
    response.raise_for_status()  # Raise exception for bad status codes

    # Print response
    print(response.text)

except requests.exceptions.RequestException as e:
    print(f"Error making API request: {e}")
except ValueError as e:
    print(f"Error parsing response: {e}")