
import requests
from bs4 import BeautifulSoup
import sys

# BBC News URL
URL = "https://www.bbc.com/news"

# Browser User-Agent
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0.0.0 Safari/537.36"
}

try:
    # Step 1: Fetch webpage
    response = requests.get(URL, headers=headers, timeout=10)

    # Step 2: Check status code
    response.raise_for_status()

    # Step 3: Parse HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # Step 4: Find headlines
    items = soup.select('h2[data-testid="card-headline"]')

    headlines = []
    seen = set()

    # Step 5: Clean and collect unique headlines
    for item in items:
        headline = item.get_text(" ", strip=True)

        if headline and headline not in seen:
            headlines.append(headline)
            seen.add(headline)

        if len(headlines) == 5:
            break

    # Step 6: Print results
    if headlines:
        for i, headline in enumerate(headlines, 1):
            print(f"{i}. {headline}")

    if len(headlines) < 5:
        print(
            f"Only {len(headlines)} headlines found. "
            "Expected 5.",
            file=sys.stderr
        )

except requests.exceptions.RequestException as e:
    print(f"Request error: {e}", file=sys.stderr)

except Exception as e:
    print(f"Error: {e}", file=sys.stderr)
