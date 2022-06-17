# Projects website

## Build

docker build -t projectswebsite:0.0.1 .

**Important:** Make sure you have a `.env` file in the same directory as this README.md and that file should contain:

```txt
PG_PASSWORD=actual-password-here (use the rdonly account for safety)
```