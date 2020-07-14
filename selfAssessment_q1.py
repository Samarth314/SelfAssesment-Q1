from requests import get
from bs4 import BeautifulSoup
import pandas as pd

url = 'http://www.imdb.com/search/title?release_date=2017&sort=num_votes,desc&page=1'
response = get(url)
print(response.text[:500])



html_soup = BeautifulSoup(response.text, 'html.parser')
type(html_soup)

movie_containers = html_soup.find_all('div', class_ = 'lister-item mode-advanced')
print(type(movie_containers))
print(len(movie_containers))

first_movie = movie_containers[0]
# first_movie

# first_movie.div

# first_movie.a

# first_movie.h3

# first_movie.h3.a

first_name = first_movie.h3.a.text

first_year = first_movie.h3.find('span', class_ = 'lister-item-year text- muted unbold ')


print(first_movie.strong)

first_imdb = float(first_movie.strong.text)
print("IMDB= ", first_imdb)

first_mscore = first_movie.find('span', class_ = 'metascore favorable')

first_mscore = int(first_mscore.text)
print ("First MetaScore", first_mscore)

first_votes = first_movie.find('span', attrs = {'name':'nv'})
first_votes['data-value']
first_votes = int(first_votes['data-value'])
print ("First_Votes=",first_votes)

eighth_movie_mscore = movie_containers[7].find('div', class_ = 'ratings-metascore')
type(eighth_movie_mscore)


names = []
years = []
imdb_ratings = []
metascores = []
votes = []

for container in movie_containers:

    if container.find('div', class_ = 'ratings-metascore') is not None:

      name = container.h3.a.text
      names.append(name)

      year = container.h3.find('span', class_ = 'lister-item-year').text
      years.append(year)

      imdb = float(container.strong.text)
      imdb_ratings.append(imdb)

      m_score = container.find('span', class_ = 'metascore').text
      metascores.append(int(m_score))

      vote = container.find('span', attrs = {'name':'nv'})['data-value']
      votes.append(int(vote))


test_df = pd.DataFrame({
                   'movie': names,
                   'year': years,
                   'imdb': imdb_ratings,
                   'metascore': metascores,
                   'votes': votes})
print(test_df.info())
print (test_df)