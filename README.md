## Create JSON

A python script to generate a database.json file, it walks thought all the files from the [CWD](https://en.wikipedia.org/wiki/Working_directory) and all its [Subdirectories](https://www.computerhope.com/jargon/s/subdirec.htm) and collects info from all the [.mp4](https://en.wikipedia.org/wiki/MPEG-4_Part_14) files.


## Requirements

1. [Python](https://www.python.org/) 3.7 and above with pip.
2. All files must follow [this](#Naming-Scheme) naming scheme
3. The Python Modules [Tabulate](https://pypi.org/project/tabulate/) & [Requests](https://pypi.org/project/requests/).
4. An API v3 key for [theMovieDB](https://www.themoviedb.org/settings/api).



## USAGE

1. Place the script in the root folder of all your anime.

2. Open a command window at that same directory

3. Type ``python create_json.py`` and hit the [RETURN](https://pc.net/helpcenter/answers/keyboard_return_key#:~:text=The%20Return%20key%20has%20the,paper%20to%20the%20next%20line) key.

4. The script will make searches to [AniList](https://anilist.co) and print a pretty table. The user will be prompted to select a number.

5. When all the unknown anime are searched and found the script will save a database.json with [this](#JSON-Structure) structure, it will also save another JSON file with all the known anime, so that on the 2nd run and onwards it won't search again for the same anime, only for the unknown ones.




## Naming Scheme

```
/Anime
	/Season {Number}
		Anime S{Number}E{Number}.mp4
```

Where ``{Number}`` is a full number, in other words an Integer.

```
S{Number} ==> S01 (Season 1)

E{Number} ==> E01 (Episode 1)
```

For Example:

```
/One-Punch Man
	/Season 1
		One-Punch Man S01E01.mp4
		One-Punch Man S01E02.mp4
```

## JSON Structure

The database.json will look like this:

```json
{
    "99263":{
        "Seasons":[
            {
                "Episodes":[
                    {
                        "ep":"01",
                        "file":"./The Rising of the Shield Hero/Season 1/The Rising of the Shield Hero S01E01.mp4"
                    },
                    {
                        "ep":"02",
                        "file":"./The Rising of the Shield Hero/Season 1/The Rising of the Shield Hero S01E02.mp4"
                    },
                    {
                        "ep":"03",
                        "file":"./The Rising of the Shield Hero/Season 1/The Rising of the Shield Hero S01E03.mp4"
                    },
                    {
                        "ep":"04",
                        "file":"./The Rising of the Shield Hero/Season 1/The Rising of the Shield Hero S01E04.mp4"
                    },
                    {
                        "ep":"05",
                        "file":"./The Rising of the Shield Hero/Season 1/The Rising of the Shield Hero S01E05.mp4"
                    }
                ]
            }
        ]
    }
}
```

It has the anilist id as the key entry, and inside it a json that has an array of seasons with their files.
