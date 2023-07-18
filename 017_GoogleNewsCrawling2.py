from GoogleNews import GoogleNews

googlenews = GoogleNews(lang='en', start='07/10/2023', end='07/17/2023')
googlenews.search('RPA solution')
googlenews.results(sort=True)

texts = googlenews.get_texts()
links = googlenews.get_links()

for i in range(len(texts)):
    print(texts[i], links[i])