import requests
from parsel import Selector

def fetch(url):
  try:
    result = requests.get(url, timeout=3)
    if result.status_code == 200:
      return result.text
    else:
      return None
  except TimeoutError:
    return None
  

def get_quotes():
  content = fetch("http://quotes.toscrape.com/")
  selector = Selector(text=content)
  quotes = selector.css("div.quote").getall()
  parsed_quotes = []
  for quote in quotes:
    quote_selector = Selector(text=quote)
    found_text = quote_selector.css("span.text::text").get()
    found_author = quote_selector.css("small.author::text").get()
    text = "".join(found_text).strip()
    author = "".join(found_author).strip()
    parsed_quotes.append(f'{text} - {author}\n')

  with open("my-quotes.txt", "w", encoding="utf-8") as file:
    for quote in parsed_quotes:
      file.write(quote)




if __name__ == "__main__":
  get_quotes()