import requests
from bs4 import BeautifulSoup

def scrape_wikipedia_page(subject):
    # Format the subject for the Wikipedia URL
    formatted_subject = subject.replace(" ", "_")
    url = f"https://en.wikipedia.org/wiki/{formatted_subject}"

    # Send a GET request to the Wikipedia page
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the main content of the page
    main_content = soup.find(id="mw-content-text")

    # Find the first non-empty paragraph within the main content
    paragraphs = main_content.find_all("p")
    first_paragraph = next((p for p in paragraphs if p.get_text(strip=True)), None)

    if first_paragraph:
        # Extract the text content of the first paragraph
        text = first_paragraph.get_text()
        return text.strip()
    else:
        return "No information found for the given subject."

# Prompt the user to enter the subject
subject = input("Enter the subject to display from Wikipedia: ")

# Scrape and display the first section of the Wikipedia page
section_text = scrape_wikipedia_page(subject)

# Print the section text
print(f"\nFirst Section of {subject}:\n{section_text}")
