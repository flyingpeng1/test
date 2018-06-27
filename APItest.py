import requests, json

#resp = requests.get("http://www.omdbapi.com/?i=tt0076759&apikey=2eb36f8a")
askAgain = "y"
while(askAgain == "y"):
  print("Enter a movie title")
  search = raw_input()
  try:
    resp = requests.get("http://www.omdbapi.com/?t=" + search +"&apikey=2eb36f8a")
    print(resp.status_code)
    print(resp.url)
    movie = eval(resp.text)
    print(movie["Title"] + " has an IMDB rating of " + movie["imdbRating"])
  except:
    print("error")
  print("Continue? (y/n)")
  askAgain= raw_input()
