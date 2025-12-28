### Pulse - Module Extraction AI Agent 🚀

**Pulse** is an intelligent, AI-powered tool designed to crawl technical documentation websites and extract a structured hierarchy of **Modules** and **Submodules**. By leveraging Large Language Models (LLMs) via Groq or OpenAI, it generates detailed descriptions for every component, converting unstructured web pages into clean, organized JSON data.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-red)
![AI](https://img.shields.io/badge/AI-Groq%2FOpenAI-green)

## 🌟 Features

* **🕷️ Intelligent Crawling:** Recursively crawls documentation pages, handling internal links and respecting domain boundaries.
* **🧠 AI-Powered Analysis:** Uses advanced LLMs (Groq Llama 3 or OpenAI GPT) to "read" the documentation and infer logical module structures.
* **🧹 Smart Filtering:** Automatically removes non-content elements like navigation bars, footers, and scripts to ensure clean data extraction.
* **📊 Interactive UI:** Built with **Streamlit** for a simple, user-friendly web interface.
* **🛡️ Robustness:** Includes browser masquerading headers and SSL verification bypass to handle strict websites.

## 🛠️ Tech Stack

* **Language:** Python 3.x
* **Frontend:** Streamlit
* **AI/LLM:** Groq API (Llama 3) / OpenAI API
* **Scraping:** Requests, BeautifulSoup4, urllib3
* **Data Format:** JSON

## 📂 Project Structure

```text
📁 pulse-module-extractor
├── main.py            # Entry point for the Streamlit App
├── crawler.py         # Logic for crawling and fetching pages
├── extractor.py       # Orchestrates the data flow (Crawler -> AI)
├── utils.py           # API handling for Groq/OpenAI
├── parser.py          # HTML cleaning and text extraction
├── requirements.txt   # Python dependencies
└── README.md          # Project documentation

```

## 🚀 Installation & Setup

1. **Clone the repository:**
```bash
git clone [https://github.com/your-username/pulse-module-extractor.git](https://github.com/your-username/pulse-module-extractor.git)
cd pulse-module-extractor

```


2. **Install dependencies:**
```bash
pip install -r requirements.txt

```


3. **Get a Free API Key:**
* Visit [Groq Console](https://console.groq.com) and create a free API Key (starts with `gsk_`).



## 🏃 Usage

1. **Run the Application:**
```bash
streamlit run main.py

```


2. **Using the App:**
* Open your browser to `http://localhost:8501`.
* **Sidebar:** Paste your Groq API Key.
* **Input:** Enter the documentation URL (e.g., `https://requests.readthedocs.io/en/latest/`).
* Click **🚀 Start Extraction**.


3. **Output:**
* View the extracted JSON structure directly in the app.
* Download the result as a `modules.json` file.



## 🧪 Tested URLs

This tool has been verified with the following documentation sites:

* ✅ **Requests Docs:** `https://requests.readthedocs.io/en/latest/`
* ✅ **Python Docs:** `https://docs.python.org/3/`
* ✅ **Chargebee:** `https://www.chargebee.com/docs/2.0/`


## 🤝 Contributing

Contributions are welcome! Please fork this repository and submit a pull request for any features, bug fixes, or enhancements.


```

```
