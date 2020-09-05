## Create JSON

A python script to generate a database.json file, it walks thought all the files from the [CWD](https://en.wikipedia.org/wiki/Working_directory) and all its [Subdirectories](https://www.computerhope.com/jargon/s/subdirec.htm) and collects info from all the [.mp4](https://en.wikipedia.org/wiki/MPEG-4_Part_14) files.

## Disclaimer
This project uses both the AniList and theMovieDB API's, thanks to tmdb I can take all the usefull episode metadata!
![tmdb](https://www.themoviedb.org/assets/2/v4/logos/v2/blue_square_1-5bdc75aaebeb75dc7ae79426ddd9be3b2be1e342510f8202baf6bffa71d7f5c4.svg | width=100)

## Requirements

1. [Python](https://www.python.org/) 3.7 and above with pip.
2. All files must follow [this](#Naming-Scheme) naming scheme
3. The Python Modules [Tabulate](https://pypi.org/project/tabulate/), [Requests](https://pypi.org/project/requests/) & [tmdb_simple](https://pypi.org/project/tmdbsimple/).
4. An API v3 key for [theMovieDB](https://www.themoviedb.org/settings/api).



## USAGE

1. Place the script in the root folder of all your anime.

2. Open the script with any text editor and replace TMDB_API_v3_KEY with your API key (PS: make sure the api key is quoted.)

3. Open a command window at that same directory

4. Type ``python create_json.py`` and hit the [RETURN](https://pc.net/helpcenter/answers/keyboard_return_key#:~:text=The%20Return%20key%20has%20the,paper%20to%20the%20next%20line) key.

5. The script will make searches to [AniList](https://anilist.co) and print a pretty table. The user will be prompted to select a number.

6. When all the unknown anime are searched and found the script will save a database.json with [this](#JSON-Structure) structure, it will also save another JSON file with all the known anime, so that on the 2nd run and onwards it won't search again for the same anime, only for the unknown ones.




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
    "83097": {
        "Seasons": [
            {
                "Episodes": [
                    {
                        "ep": "01",
                        "file": "H:/Anime/Yakusoku_no_Neverland/Yakusoku no Neverland S01E01.mp4",
                        "directory": "H:/Anime/Yakusoku_no_Neverland",
                        "season_num": "01",
                        "thumb": "http://image.tmdb.org/t/p/w1280_and_h720_bestv2/b9hFk5kwRcFUorxLQsOHasJnbDH.jpg",
                        "title": "121045"
                    },
                    {
                        "ep": "02",
                        "file": "H:/Anime/Yakusoku_no_Neverland/Yakusoku no Neverland S01E02.mp4",
                        "directory": "H:/Anime/Yakusoku_no_Neverland",
                        "season_num": "01",
                        "thumb": "http://image.tmdb.org/t/p/w1280_and_h720_bestv2/tSoiDOI9gb8gcRn14yEADvwytGj.jpg",
                        "title": "131045"
                    },
                    {
                        "ep": "03",
                        "file": "H:/Anime/Yakusoku_no_Neverland/Yakusoku no Neverland S01E03.mp4",
                        "directory": "H:/Anime/Yakusoku_no_Neverland",
                        "season_num": "01",
                        "thumb": "http://image.tmdb.org/t/p/w1280_and_h720_bestv2/kSTA7gukRLXcTDBRUfv7yedppSa.jpg",
                        "title": "181045"
                    },
                    {
                        "ep": "04",
                        "file": "H:/Anime/Yakusoku_no_Neverland/Yakusoku no Neverland S01E04.mp4",
                        "directory": "H:/Anime/Yakusoku_no_Neverland",
                        "season_num": "01",
                        "thumb": "http://image.tmdb.org/t/p/w1280_and_h720_bestv2/qCVsxLkXVZAYtWd1J0vf6Y3BBQu.jpg",
                        "title": "291045"
                    },
                    {
                        "ep": "05",
                        "file": "H:/Anime/Yakusoku_no_Neverland/Yakusoku no Neverland S01E05.mp4",
                        "directory": "H:/Anime/Yakusoku_no_Neverland",
                        "season_num": "01",
                        "thumb": "http://image.tmdb.org/t/p/w1280_and_h720_bestv2/tqBJO3K6Qfg8SCTvqY6KzVY7BdQ.jpg",
                        "title": "301045"
                    },
                    {
                        "ep": "06",
                        "file": "H:/Anime/Yakusoku_no_Neverland/Yakusoku no Neverland S01E06.mp4",
                        "directory": "H:/Anime/Yakusoku_no_Neverland",
                        "season_num": "01",
                        "thumb": "http://image.tmdb.org/t/p/w1280_and_h720_bestv2/pdlVrBEqYdAudqwdYesGzIUHuQZ.jpg",
                        "title": "311045"
                    },
                    {
                        "ep": "07",
                        "file": "H:/Anime/Yakusoku_no_Neverland/Yakusoku no Neverland S01E07.mp4",
                        "directory": "H:/Anime/Yakusoku_no_Neverland",
                        "season_num": "01",
                        "thumb": "http://image.tmdb.org/t/p/w1280_and_h720_bestv2/1TYFW08VvjK5gwBidlWk7wWCXbd.jpg",
                        "title": "011145"
                    },
                    {
                        "ep": "08",
                        "file": "H:/Anime/Yakusoku_no_Neverland/Yakusoku no Neverland S01E08.mp4",
                        "directory": "H:/Anime/Yakusoku_no_Neverland",
                        "season_num": "01",
                        "thumb": "http://image.tmdb.org/t/p/w1280_and_h720_bestv2/5JiTyxoO44tqkyzglHVfrMVF9Sb.jpg",
                        "title": "021145"
                    },
                    {
                        "ep": "09",
                        "file": "H:/Anime/Yakusoku_no_Neverland/Yakusoku no Neverland S01E09.mp4",
                        "directory": "H:/Anime/Yakusoku_no_Neverland",
                        "season_num": "01",
                        "thumb": "http://image.tmdb.org/t/p/w1280_and_h720_bestv2/8EpgmSuxcsKTB2WZTaxAuSJlD33.jpg",
                        "title": "031145"
                    },
                    {
                        "ep": "10",
                        "file": "H:/Anime/Yakusoku_no_Neverland/Yakusoku no Neverland S01E10.mp4",
                        "directory": "H:/Anime/Yakusoku_no_Neverland",
                        "season_num": "01",
                        "thumb": "http://image.tmdb.org/t/p/w1280_and_h720_bestv2/qX6DBqbQoZ9UPHbsCzCaM9GcaCm.jpg",
                        "title": "130146"
                    },
                    {
                        "ep": "11",
                        "file": "H:/Anime/Yakusoku_no_Neverland/Yakusoku no Neverland S01E11.mp4",
                        "directory": "H:/Anime/Yakusoku_no_Neverland",
                        "season_num": "01",
                        "thumb": "http://image.tmdb.org/t/p/w1280_and_h720_bestv2/jfVR52F24uiz5vl61xEHs4mzlak.jpg",
                        "title": "140146"
                    },
                    {
                        "ep": "12",
                        "file": "H:/Anime/Yakusoku_no_Neverland/Yakusoku no Neverland S01E12.mp4",
                        "directory": "H:/Anime/Yakusoku_no_Neverland",
                        "season_num": "01",
                        "thumb": "http://image.tmdb.org/t/p/w1280_and_h720_bestv2/2ly1dK8tdx2aNv5rLpjTEtPGUJ2.jpg",
                        "title": "150146"
                    }
                ],
                "pretty_title": "The Promised Neverland"
            }
        ]
    }
}
```

It has the anilist id as the key entry, and inside it a json that has an array of seasons with their files.
