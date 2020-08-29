# database.json
An python script to create a database for [FastAni](https://private.fastani.net/ "FastAni")

# Requirements
* [Files must follow the Plex naming scheme](https://support.plex.tv/articles/naming-and-organizing-your-tv-show-files/ "Files must follow the Plex naming scheme")
* [Python and pip](https://www.python.org/downloads/ "Python and pip")
* [Tabulate (pip install tabulate)](https://pypi.org/project/tabulate/ "Selenium (pip install Tabulate)")
 * [Requests (pip install requests)](https://pypi.org/project/requests/ "Requests (pip install requests)")

# Usage
1. Install Python and pip
2. Clone this repo at the root folder
3. Run ``pip install tabulate`` and ``pip install requests`` or you could do ``pip install -r requirements.txt``
4. Simply run ``python createJson.py`` in the root of your database
5. Use the CLI to select any anime the script may have problems finding
6. Use the json file generated by the script however you like

# Edits

## Variables you can change
All variables you can change are located in the config.py file. Most of them are self explanatory but here is what they do.
 
| Variables  | Description                                                                     |
|------------|---------------------------------------------------------------------------------|
| jsonPath   | Where your generated json file is saved to, by default it's '\./database\.json' |
| fileFormat | The file format which info is collected from, by default it's '\.mp4'           |


# Output

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

The databse.json will look like this:

```json
{
    "99263":{
        "Seasons":[
            {
                "Episodes":[
                    {
                        "ep":"01",
                        "file":"/media/The Rising of the Shield Hero/Season 1/The Rising of the Shield Hero S01E01.mp4"
                    },
                    {
                        "ep":"02",
                        "file":"/media/The Rising of the Shield Hero/Season 1/The Rising of the Shield Hero S01E02.mp4"
                    },
                    {
                        "ep":"03",
                        "file":"/media/The Rising of the Shield Hero/Season 1/The Rising of the Shield Hero S01E03.mp4"
                    },
                    {
                        "ep":"04",
                        "file":"/media/The Rising of the Shield Hero/Season 1/The Rising of the Shield Hero S01E04.mp4"
                    },
                    {
                        "ep":"05",
                        "file":"/media/The Rising of the Shield Hero/Season 1/The Rising of the Shield Hero S01E05.mp4"
                    }
                ]
            }
        ]
    }
}
```

It has the anilist id as the key entry, and inside it a json that has an array of seasons with their files.


### [WTFPL – Do What the Fuck You Want to Public License](http://www.wtfpl.net/ " WTFPL – Do What the Fuck You Want to Public License")
