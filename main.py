import requests
from fastapi import FastAPI

app = FastAPI()

data = requests.get('http://127.0.0.1:8000/api/Items/')
r = data.json()
data_json = []
d = []
for i in range(len(r)):
    data_json += [(r[i])]


@app.get("/{title}")
def get_category(title: str):
        return (f"The number of {title}'s category is "
                f"{([user['cat'] for user in data_json if user['title'] == title])}")
