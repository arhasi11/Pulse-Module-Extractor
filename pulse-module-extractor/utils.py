import json
from openai import OpenAI

def get_ai_response(content_chunk, api_key):
    if not api_key:
        return {"error": "No API Key provided"}

    client = OpenAI(
        api_key=api_key,
        base_url="https://api.groq.com/openai/v1"
    )

    prompt = """
    You are a technical documentation analyzer. 
    Analyze the provided text and extract a JSON structure of Modules and Submodules.
    
    Requirements:
    1. Infer top-level 'modules' from main topics.
    2. Group related 'submodules' under them.
    3. Write a detailed 'Description' for each module and submodule based on the text.
    4. OUTPUT MUST BE VALID JSON ONLY. No markdown, no code blocks.
    
    Format:
    [
        {
            "module": "Module Name",
            "Description": "...",
            "Submodules": {
                "Submodule Name": "..."
            }
        }
    ]
    """

    try:
        response = client.chat.completions.create(
            # UPDATED MODEL NAME HERE:
            model="llama-3.3-70b-versatile", 
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": f"Analyze this content:\n\n{content_chunk[:6000]}"} 
            ],
            temperature=0.3
        )
        
        content = response.choices[0].message.content.strip()
        
        if content.startswith("```json"):
            content = content.replace("```json", "").replace("```", "")
        
        return json.loads(content)
        
    except Exception as e:
        return {"error": f"AI Error: {str(e)}"}