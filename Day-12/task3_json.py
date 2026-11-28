import requests

# --- Task 1: Fetch todos and print details for the first 5 ---
print("--- Task 1: First 5 Todos ---")
todos_url = "https://jsonplaceholder.typicode.com/todos"
todos_response = requests.get(todos_url)

if todos_response.status_code == 200:
    todos = todos_response.json()
    for todo in todos[:5]:
        print(f"ID: {todo['id']} | Title: {todo['title']} | Completed: {todo['completed']}")
else:
    print("Failed to fetch todos. Status:", todos_response.status_code)


# --- Task 2: Fetch user with ID 5 and print Name & Company Name ---
print("\n--- Task 2: User 5 Details ---")
user_url = "https://jsonplaceholder.typicode.com/users/5"
user_response = requests.get(user_url)

if user_response.status_code == 200:
    user = user_response.json()
    print("User's Name:", user["name"])
    print("Company Name:", user["company"]["name"])
else:
    print("Failed to fetch user details. Status:", user_response.status_code)


# --- Task 3: Function to fetch a specific post by post_id ---
print("\n--- Task 3: Post Details Function ---")
def get_post_details(post_id):
    post_url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    response = requests.get(post_url)
    if response.status_code == 200:
        return response.json()
    return {"error": f"Failed with status code {response.status_code}"}

result = get_post_details(12)
print("Post 12 Result:", result)