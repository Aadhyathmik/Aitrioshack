import requests
import streamlit as st

device_mapping = {
        "11041_f0a": "Aid-80070001-0000-2000-9002-000000000f0a",
        "11043_f0c_Aadi": "Aid-80070001-0000-2000-9002-000000000f0c",
        "11044_f0d": "Aid-80070001-0000-2000-9002-000000000f0d",
        "11048_f11_jay": "Aid-80070001-0000-2000-9002-000000000f11",
        "11049_f12_Raj": "Aid-80070001-0000-2000-9002-000000000f12",
        "11061_f1e": "Aid-80070001-0000-2000-9002-000000000f1e",
        "11063_f20": "Aid-80070001-0000-2000-9002-000000000f20",
        "11064_f21": "Aid-80070001-0000-2000-9002-000000000f21",
        "11065_f22_Blake": "Aid-80070001-0000-2000-9002-000000000f22",
        "11067_f24_tanush": "Aid-80070001-0000-2000-9002-000000000f24",
        "11070_f27": "Aid-80070001-0000-2000-9002-000000000f27"
    }

def fetch_api_data(api_url):
    """
    Fetch JSON data from the given API URL.
    """
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an error for bad status codes
        return response.json()       # Parse and return JSON content
    except requests.exceptions.RequestException as e:
        st.error(f"An error occurred: {e}")
        return None
    
def main():
    st.title("Device Data Viewer")

    # Create a select box using the keys from the device_mapping dictionary.
    selected_display = st.selectbox("Select Device:", list(device_mapping.keys()))

    # When the "Fetch Data" button is clicked, use the corresponding device ID
    if st.button("Fetch Data"):
        actual_device_id = device_mapping.get(selected_display)
        st.write(f"Fetching data for Device ID: {actual_device_id}")

        api_url="https://2c52-64-79-113-53.ngrok-free.app/devices/"+actual_device_id+"/result"
        # Construct the API URL with the actual device ID.
        # Replace the URL with your actual API endpoint.
        #api_url = "https://2c52-64-79-113-53.ngrok-free.app/devices/"+actual_device_id/result"
        
        data = fetch_api_data(api_url)
        if data:
            st.subheader("JSON Result Data")
            st.json(data)  # Display JSON in a pretty format
        else:
            st.error("Failed to retrieve data.")

if __name__ == "__main__":
    main()
