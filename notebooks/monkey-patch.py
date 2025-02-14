import requests

# Original function
original_get = requests.get

def patched_get(url, *args, **kwargs):
    print(f"Requesting URL: {url}")
    response = original_get(url, *args, **kwargs)
    print(f"Response Status Code: {response.status_code}")
    return response

# Apply the monkey patch
requests.get = patched_get

# Use the patched requests.get
response = requests.get('https://api.github.com')
print(response.json())

# Revert the monkey patch
requests.get = original_get

# Use the original requests.get
response = requests.get('https://api.github.com')
print(response.json())