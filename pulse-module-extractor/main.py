import streamlit as st
import json
from crawler import crawl_site
from extractor import extract_modules

st.set_page_config(page_title="Pulse Module Extractor", layout="wide")
st.title("Pulse - Module Extraction AI Agent")

with st.sidebar:
    st.header("Settings")
    api_key = st.text_input("OpenAI API Key", type="password")

st.subheader("Input")
url_input = st.text_area("Enter Documentation URLs (one per line):", height=100, 
                        placeholder="[https://help.instagram.com/](https://help.instagram.com/)")

if st.button("🚀 Start Extraction"):
    if not api_key:
        st.error("Please enter an API Key in the sidebar.")
    elif not url_input:
        st.error("Please enter at least one URL.")
    else:
        urls = [line.strip() for line in url_input.split('\n') if line.strip()]
        
        with st.status("🕷️ Crawling documentation...", expanded=True) as status:
            st.write(f"Targeting: {urls}")
            raw_data = crawl_site(urls)
            st.write(f"✅ Successfully crawled {len(raw_data)} pages.")
            
            st.write("🧠 Processing with AI...")
            final_structure = extract_modules(raw_data, api_key)
            status.update(label="Extraction Complete!", state="complete", expanded=False)

        st.subheader("Extracted Structure")
        
        if isinstance(final_structure, dict) and "error" in final_structure:
            st.error(f"AI Error: {final_structure['error']}")
        else:
            st.json(final_structure)
            
            st.download_button(
                label="📥 Download JSON",
                data=json.dumps(final_structure, indent=2),
                file_name="modules.json",
                mime="application/json"
            )