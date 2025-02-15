import requests

# URL of your FastAPI app (replace with your actual URL if different)
url = "http://127.0.0.1:8000/predict"

# Example query to test
query = "The patient is experiencing unexplained weight loss, increased thirst, and frequent urination. His blood pressure is 130/85 mmHg."
query=query+"What conditions could explain these symptoms?"
print(query)
# Send a GET request to the FastAPI /predict endpoint with the query
response = requests.get(url, params={"query": query})

# Check if the request was successful
if response.status_code == 200:
    # Print the response from the model
    print("Response from the model:", response.json())
else:
    print("Failed to get a response, Status Code:", response.status_code)
