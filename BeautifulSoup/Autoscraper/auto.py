#pip install autoscraper
from autoscraper import AutoScraper

# Define the URL and the list of items you want to scrape
url = "https://www.jiomart.com/c/groceries/2"
wanted_list = ["60", "Bharat Chana Dal 1 Kg"]

# Create an AutoScraper instance
scraper = AutoScraper()

# Build the scraper using the URL and the wanted list
result = scraper.build(url, wanted_list)
print(result)

# Get the results in a grouped format
grouped_results = scraper.get_result_similar(url, grouped=True)

# Set rule aliases for better readability
scraper.set_rule_aliases({'rule_vtwt': 'Price', 'rule_xj9r': 'Title'})

# Keep only the relevant rules
scraper.keep_rules(['rule_vtwt', 'rule_xj9r'])

# Save the scraper configuration
scraper.save("JioMart_Search")

# Get the final results with aliases
final_results = scraper.get_result_similar("https://www.jiomart.com/c/groceries/2", group_by_alias=True)
final_results['Price']
final_results['Title']
