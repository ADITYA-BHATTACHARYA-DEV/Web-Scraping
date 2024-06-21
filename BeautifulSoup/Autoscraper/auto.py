#pip install autoscraper
from autoscraper import AutoScraper
url="https://www.jiomart.com/c/groceries/2"
wanted_list=["60","Bharat Chana Dal 1 Kg"]
scrapper=AutoScraper()
result=scrapper.build(url,wanted_list)
print(result)
scrapper.get_result_similar(url,grouped=True)
scrapper.set_rule_aliases({'rule_vtwt':'Price','rule_xj9r':'Title'})
scrapper.keep_rules(['rule_vtwt','rule_xj9r'])
scrapper.save("Jio MArt Search")
results=scrapper.get_result_similar("https://www.jiomart.com/c/groceries/2",group_by_alias=True)
results['Price']
results['Title']