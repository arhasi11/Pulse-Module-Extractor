import requests
from urllib.parse import urljoin, urlparse
from parser import clean_html
from bs4 import BeautifulSoup
import urllib3

# Mute the warning about unverified HTTPS requests
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def crawl_site(start_urls, max_pages=10):
    if isinstance(start_urls, str):
        start_urls = [start_urls]

    visited = set()
    pages = {}
    queue = list(start_urls)
    
    # Allow crawling the domain of the first URL
    allowed_domains = {urlparse(u).netloc for u in start_urls}
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/91.0.4472.124 Safari/537.36"
    }

    while queue and len(visited) < max_pages:
        url = queue.pop(0)
        if url in visited:
            continue

        try:
            print(f"Crawling: {url}")
            # verify=False is CRITICAL for bypassing SSL blocks
            res = requests.get(url, headers=headers, timeout=10, verify=False)
            
            if res.status_code != 200:
                print(f"Status {res.status_code} for {url}")
                continue
                
            clean_text = clean_html(res.text)
            
            # Relaxed check: save page if it has ANY text
            if len(clean_text) > 50:
                pages[url] = clean_text
            
            visited.add(url)

            soup = BeautifulSoup(res.text, "html.parser")
            for link in soup.find_all("a", href=True):
                full_url = urljoin(url, link['href'])
                parsed_url = urlparse(full_url)
                
                if parsed_url.netloc in allowed_domains:
                    if full_url not in visited and full_url not in queue:
                        queue.append(full_url)

        except Exception as e:
            print(f"Error processing {url}: {e}")
            continue

    return pages