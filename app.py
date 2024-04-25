import requests


# Function to create a new post
def create_post(title, body, user_id):
    url = "https://jsonplaceholder.typicode.com/posts"
    data = {
        'title': title,
        'body': body,
        'userId': user_id
    }
    response = requests.post(url, json=data)
    if response.status_code == 201:
        print("Post created successfully.")
        return response.json()
    else:
        print(f"Failed to create post. Status code: {response.status_code}")
        return None


# Function to read all posts
def read_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch posts. Status code: {response.status_code}")
        return None


# Function to update a post by id
def update_post(post_id, title, body, userId):
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    data = {
        'title': title,
        'body': body,
        'userId': userId
    }
    response = requests.put(url, json=data)
    if response.status_code == 200:
        print(f"Post {post_id} updated successfully.")
        return response.json()
    else:
        print(f"Failed to update post {post_id}. Status code: {response.status_code}")
        return None


# Function to delete a post by id
def delete_post(post_id):
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    response = requests.delete(url)
    if response.status_code == 200:
        print(f"Post {post_id} deleted successfully.")
    else:
        print(f"Failed to delete post {post_id}. Status code: {response.status_code}")


# Example usage
# Create a new post
new_post = create_post("New Title", "New body content", 1)
print("New Post:", new_post)

# Read all posts
all_posts = read_posts()
print("All Posts:", all_posts)

# Update the first post
if all_posts:
    first_post_id = all_posts[0]['id']
    updated_post = update_post(first_post_id, "Updated Title", "Updated body content", 2)
    print("Updated Post:", updated_post)

# Delete the first post
if all_posts:
    first_post_id = all_posts[0]['id']
    delete_post(first_post_id)
