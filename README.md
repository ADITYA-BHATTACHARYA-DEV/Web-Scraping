﻿# Web-Scraping


 # Beautiful Soup is a powerful Python library used for web scraping and parsing HTML or XML documents. When scraping data from Amazon (or any other website), Beautiful Soup simplifies the process of extracting relevant information by providing an easy-to-use interface. Let’s dive into how Beautiful Soup is leveraged for scraping Amazon product data:

# **Web Scraping Basics:*
Web scraping involves fetching data from websites by making HTTP requests and then extracting specific information from the HTML content.
Beautiful Soup helps parse the HTML structure, navigate through elements, and extract relevant data.
Installation:
First, install Beautiful Soup using pip:

pip install beautifulsoup4

#Steps for Scraping Amazon Product Data:

We’ll focus on scraping product information from Amazon, but the same principles apply to other websites.
#Here are the steps:

**a.* Fetch the Webpage:* - Use the requests library to download the Amazon product page as HTML content. - Send an HTTP request to the Amazon product URL. - Example: 
   python import requests
   url = 'https://www.amazon.com/product-url'
   response = requests.get(url)
     
**b.* Parse the HTML Content:* - Create a Beautiful Soup object to parse the HTML content. - Specify the parser (usually ‘lxml’ or ‘html.parser’). - Example: 
python from bs4 import BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')
     
**c.* Locate Relevant Elements:* - Identify the HTML elements containing the data you want to scrape. - Inspect the Amazon product page (using browser developer tools) to find element IDs, classes, or other attributes. - Example: python          # Suppose we want to extract the product title          title_element = soup.find('span', attrs={'id': 'productTitle'})          product_title = title_element.text.strip()  

**d.* Extract Data:* - Use Beautiful Soup methods (such as find, find_all, or CSS selectors) to extract specific data. - Handle cases where the element may not exist (use try-except blocks). - 
Example: python 
try:              
**Extract product title**            
product_title = title_element.text.strip()          
except AttributeError:              
product_title = "NA"  # Handle missing data          
**e. Save Data:* - You can save the extracted data to a CSV file, database, or any other storage format. - Example: python          with open('amazon_product_data.csv', 'a') as csv_file:              csv_file.write(f"{product_title}\n")  

**User-Agent and Headers:*

To avoid being blocked by Amazon (or any website), set a user-agent in your HTTP request headers.
The user-agent simulates a real browser request.
Example:
Python

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}
response = requests.get(url, headers=HEADERS)


# ** Leveraging the use of LLM in Web Scraping**
 ScrapeGraphAI leverages Ollama and Rag for web scraping. These tools, combined with Large Language Models (LLMs), offer flexible and efficient scraping solutions for developers.

# **What Is ScrapeGraphAI?**
ScrapeGraphAI is an open-source Python library designed for web scraping.
It uses LLMs (such as GPT-3) and direct graph logic to create scraping pipelines.
The goal is to simplify web scraping while adapting to changes in website structures.
Leveraging LLMs with Ollama:
Ollama simplifies the process of downloading, setting up, and running LLMs.
To use LLMs in ScrapeGraphAI, follow these steps:
Pull LLMs from Ollama:
Python

# First, pull LLMs from Ollama
ollama pull llama3
ollama pull nomic-embed-text
Use them in the graph configuration:
Python

graph_config = {
    "llm": {
        "model": "llama3",
        "temperature": 0.0,
        "format": "json",
    },
    "embeddings": {
        "model": "nomic-embed-text",
    },
}

**Scraping with ScrapeGraphAI:**
ScrapeGraphAI represents scraping pipelines using a direct graph implementation.
Each node in the graph has a specific function:
Retrieve HTML from a website.
Extract relevant information based on your query.
Generate a coherent answer.
The SmartScraperGraph class is one such default scraping pipeline.
**Local Execution:**
ScrapeGraphAI can run locally, making it convenient for developers.
Minimum RAM requirements are around 15GB.
You can apply this approach not only to websites but also to local documents (XML, HTML, JSON, etc.).
Benefits of ScrapeGraphAI:
Flexibility: Adapts to website changes, reducing the need for constant developer intervention.
Low Maintenance: Remains functional even when website layouts change.
Power of LLMs: Utilizes LLMs for intelligent data extraction.

