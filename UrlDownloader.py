import requests
from requests.exceptions import RequestException
from time import sleep

def download_urls(urls):
    max_retries = 3
    results = {}

    for url in urls:
        attempts = 0
        while attempts < max_retries:
            try:
                response = requests.get(url)
                response.raise_for_status()  # Raise HTTPError for bad responses
                results[url] = response.content
                print(f"Downloaded content from {url}")
                break  # Break out of retry loop if successful
            except RequestException as e:
                attempts += 1
                print(f"Attempt {attempts} failed: {e}")
                if attempts < max_retries:
                    print(f"Retrying {url} after {attempts} seconds...")
                    sleep(attempts)  # Sleep for increasing seconds before retrying
                else:
                    print(f"Failed to download from {url} after {max_retries} attempts.")
                    results[url] = None  # Store None for failed downloads

    return results

# Function to get user input for URLs
def get_user_urls():
    urls = []
    while True:
        url = input("Enter a URL to download (or leave blank to finish): ").strip()
        if not url:
            break
        urls.append(url)
    return urls

# Example usage:
if __name__ == "__main__":
    urls = get_user_urls()
    if urls:
        results = download_urls(urls)
        for url, content in results.items():
            if content is not None:
                print(f"Content from {url}: {len(content)} bytes")
            else:
                print(f"Failed to download content from {url}")
    else:
        print("No URLs provided. Exiting.")
