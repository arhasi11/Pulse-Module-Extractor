from bs4 import BeautifulSoup

def clean_html(html_content):
    soup = BeautifulSoup(html_content, "html.parser")

    # Only remove technical tags, keep nav/footer/header for now to ensure we get text
    for tag in soup(["script", "style", "noscript", "meta", "link"]):
        tag.decompose()

    text = soup.get_text(separator=" ", strip=True)
    return text