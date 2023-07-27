# Import the required library to do the URL request, as well as scraping
import requests
from bs4 import BeautifulSoup as bs


# We initatilize by asking for the username we will be looking for
github_user = input("Input the Github User: ")
#We then generate the URL based on the usual way github generates user profile URL's
url = "https://github.com/" +github_user
r = requests.get(url)
soup = bs(r.content, "html.parser")
# Then we want to be looking for people's images and printing out the URL to their profile picture
profile_image = soup.find('img', {'alt' : 'Avatar'})['src']
print(profile_image)