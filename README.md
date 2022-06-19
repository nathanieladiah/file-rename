# Movie and TV Show File Rename

#### Video Demo: 

#### Description:

The program will be a command line program that will take files and rename them according to the Plex guidelines for streaming.

##### Movies:
```
/Movies
	/Avatar (2009)
		Avatar (2009).mkv
	/Batman Begins (2005)
		Batman Begins (2005).mp4
		Batman Begins (2005).en.srt
		poster.jpg
```

Can also use the IMDb or TheMovieDB Id number in curly braces. `{[source]-[id]}`

```
/Movies
	/Batman Begins (2005) {imdb-tt0372784}
		Batman Begins (2005) {imdb-tt0372784}.mp4
```

```
/Movies
	/Batman Begins (2005) {tmdb-272}
		Batman Begins (2005) {tmdb-272}.mp4
```

##### TV Shows

Season based:

`/TV Shows/ShowName/Season 02/ShowName-s02e17-Optional_info.ext`

Date-Based:

`/TV Shows/ShowName/Season 02/ShowName - 2011-00-15 - Optional_Info.ext`

`YYYY-MM-DD or DD-MM-YYYY`

Miniseries:

Just use `Season 01`


```
/TV Shows
	/Doctor Who (1963) {tvdb-76107}
		/Season 01
			S01e01 - An Unearthly Child (1).mp4
			S01e02 - The Cave of Skulls (2).mp4
	/From the Earth to the Moon (1998)
		/Season 01
			From the Earth to the Moon (1998) - s01e01.mp4
			From the Earth to the Moon (1998) - s01e02.mp4
	/Grey's Anatomy (2005)
	 	/Season 00
			Grey's Anatomy (2005) - s00e01 - Straight to the Heart.avi
		/Season 01
			Grey's Anatomy (2005) - s01e01 - pt1.avi
			Grey's Anatomy (2005) - s01e01 - pt2.avi
			Grey's Anatomy (2005) - s01e02 - The First Cut is the Deepest.avi
			Grey's Anatomy (2005) - s01e03.mp4
		/Season 02
			Grey's Anatomy (2005) - s02e01-e03.avi
			Grey's Anatomy (2005) - s02e04.m4v
	/The Colbert Report (2005)
		/Season 08
			The Colbert Report (2005) - 2011-11-15 - Elijah Wood.mp4
```

### Proposed Features

[ ] Rename directories and files for media to be included in plex

[ ] Use the filenames to search imdb or tmdb to get show info

