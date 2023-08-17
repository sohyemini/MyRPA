from GoogleNews import GoogleNews

# googlenews = GoogleNews(lang='en', start='08/10/2023', end='08/14/2023')
googlenews = GoogleNews(lang='en', region='US')
googlenews = GoogleNews(period='1d')
googlenews.search('new python packages')
googlenews.results(sort=True)

texts = googlenews.get_texts()
links = googlenews.get_links()

for i in range(len(texts)):
    print(texts[i], links[i])