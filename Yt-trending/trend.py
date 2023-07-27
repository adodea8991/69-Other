#to be redone
import requests
from bs4 import BeautifulSoup

# Function to scrape the YouTube trending page and extract channel names
def scrape_channels():
    url = "https://www.youtube.com/feed/trending"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    channel_elements = soup.find_all("a", class_="yt-simple-endpoint style-scope ytd-channel-name")[:20]
    channels = [channel.text.strip() for channel in channel_elements]
    return channels

# Main function
def main():
    channels = scrape_channels()
    print("Top 20 Channels:")
    for channel in channels:
        print(channel)

# Run the script
if __name__ == "__main__":
    main()
