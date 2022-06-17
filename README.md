# Projects website

## Build

docker build -t projectswebsite:0.0.1 .

**Important:** Make sure you have a `.env` file in the same directory as this README.md and that file should contain:

```txt
PG_PASSWORD=actual-password-here (use the rdonly account for safety)
```

Decent resource -- look at imdb.py to see a trick for converting results of aiosql query to pydantic model:

https://github.com/TheDataMine/f2021-stat39000-project10/blob/main/app/imdb.py

genres.append(Genre(**{key: genre for _, key in enumerate(Genre.__fields__.keys())}))

