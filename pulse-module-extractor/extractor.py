from utils import get_ai_response

def extract_modules(pages_data, api_key):
    full_context = ""
    for url, text in pages_data.items():
        full_context += f"Source: {url}\nContent: {text[:2000]}\n\n"
    
    if not full_context:
        return {"error": "No content found. The crawler might have been blocked."}

    result = get_ai_response(full_context, api_key)
    
    return result