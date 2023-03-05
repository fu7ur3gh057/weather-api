# Weather

## Docker

Run this application with docker

```bash
docker compose build
docker compose up -d
```

## API

Use this url path for getting data

```bash
GET request
0.0.0.0:8000/weather/now/
body : {location:"moscow"}
```

```bash
GET request
0.0.0.0:8000/weather/forecast/
body : {days:2, location:"moscow"}
```
