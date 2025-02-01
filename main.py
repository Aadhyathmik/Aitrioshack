import requests

def fetch_api_data(api_url):
    """
    Fetch JSON data from the given API URL.
    """
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an error for bad status codes
        return response.json()       # Parse and return JSON content
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def main():
    # Replace with your actual API endpoint URL
    api_url = "https://2c52-64-79-113-53.ngrok-free.app/devices/Aid-80070001-0000-2000-9002-000000000f12/result"
  
    
    data = fetch_api_data(api_url)
    if data is None:
        print("Failed to retrieve data from the API.")
        return

    # Print the entire JSON response
    print("Full JSON response:")
    print(data)
    print()

    # Extract and print individual fields from the JSON
    timestamp = data.get("timestamp")
    device_id = data.get("deviceId")
    model_id = data.get("modelId")
    detected_objects = data.get("detectedObjects", [])

    print(f"Timestamp: {timestamp}")
    print(f"Device ID: {device_id}")
    print(f"Model ID: {model_id}")
    print("Detected Objects:")

    for index, obj in enumerate(detected_objects, start=1):
        class_id = obj.get("class_id")
        score = obj.get("score")
        left = obj.get("left")
        top = obj.get("top")
        right = obj.get("right")
        bottom = obj.get("bottom")
        
        print(f"  Object {index}:")
        print(f"    Class ID: {class_id}")
        print(f"    Score: {score}")
        print(f"    Bounding Box: left={left}, top={top}, right={right}, bottom={bottom}")

if __name__ == "__main__":
    main()
