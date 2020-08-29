import requests
import json
import os
from io import StringIO
from tabulate import tabulate
from config import *

#
# No need to understand what the function below does, it just uses the anilist api 
#and creates a "table" using tabulate with the anilist results
#

def search_anilist(search, max_results=50):
    query = """
    query ($id: Int, $page: Int, $search: String, $type: MediaType) {
            Page (page: $page, perPage: 50) {
                    media (id: $id, search: $search, type: $type) {
                            id
                            title {
                                    english
                                    romaji
                            }}}}"""
    
    variables = {
            'search': search,
            'page': 1,
            'perPage': max_results,
            'type': 'ANIME'
    }

    response = requests.post(url, json={'query': query, 'variables': variables})
    io = StringIO(response.text)
    results = json.load(io)
    result_list = results['data']['Page']['media']
    final_result = []
    count = 0
    for anime in result_list:
        jp_title = anime['title']['romaji']
        ani_id = anime['id']

        entry = [count, jp_title, ani_id]
        final_result.append(entry)
        count += 1
    headers = ['SlNo', "Title", "id"]
    table = tabulate(final_result, headers, tablefmt='psql')
    table = '\n'.join(table.split('\n')[::-1])
    return table, final_result

#
#This function parses the filename string to extract all the info the 
#database may need. It returns a tuple with: 
#    the title, 
#    the season number 
#    and a dictionary with episode info.
#

def extract_info(filename, directory):
    try:
        title = filename.split(' ')
        misc = title.pop(-1).split('.')[0]
        season_num = misc.split('E')[0].replace('S', '')
        episode_num = misc.split('E')[1]
        title = ' '.join(title).split('\\')[-1].split('/')[-1]
        return title, season_num, {'ep': episode_num, 'file': os.path.abspath(os.path.join(directory.replace('\\', '/'), filename)).replace('\\', '/').replace('/var/www/html/', 'https://private.fastani.net/')}
    except IndexError:
        return

#
#This function creates a dict with the layout that is desired
#All the try excepts are to make that dict, 
#because it will error if a key is missing 
#thats why i have try except blocks to make the necessary and only needed keys
#

def add_json(files, gg):
    for a in files:
        f = extract_info(a[0], a[1])
        if type(f) == type(None):
            continue
        title, season, eps = f
        try:
            ff = id_to_anime[title]
        except KeyError:
            table, ff = search_anilist(title)
            print(f'Search results for {title} season {season}')
            print(table)
            num = input("Select number: [0]: ")
            try:
                num = int(num)
            except ValueError:
                num = 0
            if num <= 50:
                choice = ff[num] if num != '' else ff[0]
                ff = str(choice[-1])
            else:
                ff = num
            id_to_anime[title] = ff
        try:
            try:
                gg[ff]['Seasons'][season]['Episodes'].append(eps)
            except:
                gg[ff]['Seasons'][season] = {}
                gg[ff]['Seasons'][season]['Episodes'] = []
        except:
            try:
                gg[ff]['Seasons'] = {}
                gg[ff]['Seasons'][season] = {}
                gg[ff]['Seasons'][season]['Episodes'] = []
                gg[ff]['Seasons'][season]['Episodes'].append(eps)
            except KeyError:
                gg[ff] = {}
                gg[ff]['Seasons'] = {}
                gg[ff]['Seasons'][season] = {}
                gg[ff]['Seasons'][season]['Episodes'] = []
                gg[ff]['Seasons'][season]['Episodes'].append(eps)

#
#This function is responsible for 
#1. taking the Seasons dict inside the generated dict from the above function
#2. Converting it to an array
#3. Sort the array to the correct seasons order
#

def conv_list(gg):
    for a, b in id_to_anime.items():
        seasons = gg[b]['Seasons']
        fg = []
        for c, d in seasons.items():
            fg.append(d)
        fg = sorted(fg, key=lambda entry: int(entry['Episodes'][0]['file'].split(' ').pop(-1).split('.')[0].split('E')[0].replace('S', '')))
        gg[b]['Seasons'] = fg

#
#This function just saves the provided dict to a json file
#

def save_to_json(data, path=jsonPath):
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)

#
#This for loop makes a list 
#with all the .mp4 files from the Current Working Directory
#and all the subdirectories
#

for directory, __, files in os.walk(".", topdown=True):
    for file in files:
        if file.endswith('.mp4'):
            files_list.append([file, directory])

hh = {}
add_json(files_list, hh)
conv_list(hh)
save_to_json(hh)