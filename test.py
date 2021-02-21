import requests

BASE = "http://127.0.0.1:5000/"
#data = [
#{"name": "First video", "views": 0, "likes": 10},
#{"name": "Second video", "views": 0, "likes": 10},
#{"name": "Third video", "views": 0, "likes": 10},
#{"name": "Fourth video", "views": 0, "likes": 10}
#]
#for i in range(len(data)):
#   response = requests.put(BASE + 'video/' +str(i), data[i])    
#    print(response.json())


#input()
response = requests.patch(BASE + "video/0", {"name": "My first updated video"})
print(response.json())
