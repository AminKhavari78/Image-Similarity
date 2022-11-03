# Get api for find similarity between 2 image
import requests
r = requests.post(
    "https://api.deepai.org/api/image-similarity",
    files={
        'image1': open('/home/amin/PycharmProjects/Think/videostreaming/download.jpeg', 'rb'),
        'image2': open('/home/amin/PycharmProjects/Think/videostreaming/download (1).jpeg', 'rb'),
    },
    headers={'api-key': 'quickstart-QUdJIGlzIGNvbWluZy4uLi4K'}
)
print(r.json())