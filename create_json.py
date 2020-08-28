import requests
from io import StringIO
import json
from tabulate import tabulate


#####################################################################
def search_anilist(search, max_results=50):
    query = """
    query ($id: Int, $page: Int, $search: String, $type: MediaType) {
            Page (page: $page, perPage: 50) {
                    media (id: $id, search: $search, type: $type) {
                            id
                            title {
                                    english
                                    romaji
                            }
                    }
            }
    }
    """
    variables = {
            'search': search,
            'page': 1,
            'perPage': max_results,
            'type': 'ANIME'
    }
    url = 'https://graphql.anilist.co'

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
#####################################################################
# No need to understand what the above does, 
# it just uses the anilist api and creates a "table" using tabulate with the anilist results


import os

def extract_info(filename, directory):
    """
    This function parses the filename string to extract all the info
    the database may need. It returns a tuple with: 
        the title, 
        the season number 
        and a dictionary with episode info.
    """
    try:
        title = filename.split(' ')
        misc = title.pop(-1).split('.')[0]
        season_num = misc.split('E')[0].replace('S', '')
        episode_num = misc.split('E')[1]
        title = ' '.join(title).split('\\')[-1].split('/')[-1]
        return title, season_num, {'ep': episode_num, 'file': os.path.abspath(os.path.join(directory.replace('\\', '/'), filename)).replace('\\', '/').replace('/var/www/html/', 'https://private.fastani.net/')}
    except IndexError:
        return
    
id_to_anime = {}

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

def conv_list(gg):
    for a, b in id_to_anime.items():
        seasons = gg[b]['Seasons']
        fg = []
        for c, d in seasons.items():
            fg.append(d)
        fg = sorted(fg, key=lambda entry: int(entry['Episodes'][0]['file'].split(' ').pop(-1).split('.')[0].split('E')[0].replace('S', '')))
        gg[b]['Seasons'] = fg


def save_to_json(data, path='./database.json'):
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)

files_list = []

for directory, __, files in os.walk(".", topdown=True):
    for file in files:
        if file.endswith('.mp4'):
            files_list.append([file, directory])
hh = {}
add_json(files_list, hh)
conv_list(hh)
save_to_json(hh)
