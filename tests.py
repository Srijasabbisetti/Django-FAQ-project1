import requests

def test_api_endpoints():
    # Test API Root
    try:
        print("\nTesting API Root...")
        response = requests.get("http://127.0.0.1:8000/api/")
        response.raise_for_status()  # Raise HTTPError for bad status codes
        print(f"Status Code: {response.status_code}")
        print("API Root Response:", response.json())
    except requests.exceptions.RequestException as e:
        print(f"Error in API Root: {str(e)}")

    # Test FAQs List
    try:
        print("\nTesting FAQs List...")
        response = requests.get("http://127.0.0.1:8000/api/faqs/")
        response.raise_for_status()
        print(f"Status Code: {response.status_code}")
        print("FAQs List Response:", response.json())
    except requests.exceptions.RequestException as e:
        print(f"Error in FAQs List: {str(e)}")

if __name__ == "__main__":
    test_api_endpoints()