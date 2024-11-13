import requests
from bs4 import BeautifulSoup

# Step 1: Send a GET request to the website
url = "http://quotes.toscrape.com/"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    print("Successfully retrieved the webpage!")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

# Step 2: Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Step 3: Extract quotes and authors
quotes_data = []  # List to hold the data

# Find all quote blocks on the page
for quote_block in soup.find_all("div", class_="quote"):
    # Extract the text of the quote
    quote_text = quote_block.find("span", class_="text").get_text()
    
    # Extract the author of the quote
    author = quote_block.find("small", class_="author").get_text()
    
    # Append each quote and author as a formatted string to the list
    quotes_data.append(f"{quote_text} - {author}")

# Step 4: Save the data to a text file
with open("quotes.txt", "w", encoding="utf-8") as file:
    for item in quotes_data:
        file.write(item + "\n\n")  # Write each quote with an extra newline for readability

print("Quotes saved to quotes.txt")
