from gnews import GNews


site_cnbc = "CNBC.com"
site_bloomberg = "bloomberg.com"
test = GNews.get_news_by_site(self=GNews(), site=site_bloomberg)


print(test[0])
