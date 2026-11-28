import requests

# --- Task 1: Concept Answers (in comments) ---
# 1. Client vs Server: A Client (browser or Python script) sends a request for information,
#    while a Server receives that request, processes it, and sends back the requested data.
# 2. HTTP GET Request: An HTTP GET request asks a server to retrieve and return specific
#    data or a webpage without making changes on the server.

# --- Task 2: Send GET request to httpbin.org/status/404 and handle status code ---
print("--- Task 2: Handling 404 Status ---")
url_404 = "https://httpbin.org/status/404"
response = requests.get(url_404)

print("Status Code:", response.status_code)
if response.status_code == 200:
    print("Success! Page found.")
elif response.status_code == 404:
    print("Error 404: The requested page or resource was not found on the server.")
else:
    print(f"Request failed with status code: {response.status_code}")

# --- Task 3: Check if a user-provided website URL is online ---
print("\n--- Task 3: Website Status Checker ---")
user_url = input("Enter a website URL (e.g., https://www.github.com): ").strip()

try:
    site_response = requests.get(user_url, timeout=5)
    if site_response.status_code == 200:
        print("Website is Online")
    else:
        print("Website is Offline")
except requests.exceptions.RequestException as e:
    print("Website is Offline (Invalid URL or connection failed)")