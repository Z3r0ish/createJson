import tmdbsimple as tmdb

jsonPath = './database.json'
jsonConfig = './config.json'
fileFormat = '.mp4'
tmdb.API_KEY = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

#
# Don't mess with these
#
files_list = []
id_to_anime = {}
url = 'https://graphql.anilist.co'
