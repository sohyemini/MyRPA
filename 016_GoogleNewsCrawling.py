from GoogleNews import GoogleNews

googlenews = GoogleNews(lang='en', period='1d')
googlenews.search('RPA solution')
googlenews.results(sort=True)

texts = googlenews.get_texts()
links = googlenews.get_links()

print(texts)
print(links)
print(len(texts))