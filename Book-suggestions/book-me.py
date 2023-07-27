#not finished
import requests
from bs4 import BeautifulSoup

def get_book_titles(genre):
    url = f"https://www.goodreads.com/genres/{genre}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    book_titles = soup.find_all("a", class_="readable bookTitle")
    return [title.get_text(strip=True) for title in book_titles]

def display_book_titles(genre):
    book_titles = get_book_titles(genre)
    print(f"Book titles in the {genre} genre:")
    for i, title in enumerate(book_titles, start=1):
        print(f"{i}. {title}")

if __name__ == "__main__":
    genre = input("Please choose a genre (business/romance/science/history): ")
    display_book_titles(genre)
