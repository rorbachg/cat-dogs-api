# cat-dogs-api
How to run it:
1. Pull docker image

  `docker pull rorbachg/cats-dogs-api:main`
  
2. Start docker container

`docker run --name cats-dogs-api -p 80:80 cats-dogs-api`

3. See docs at `http://localhost:80/v1/redoc`
4. Query local endpoint:

```
curl --location --request POST 'localhost:80/v1/predict/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "urls": [
        "https://upload.wikimedia.org/wikipedia/commons/1/15/Cat_August_2010-4.jpg",
        "https://cdn.britannica.com/86/166986-050-4CEFE5DE/cute-kitten-and-puppy-outdoors-in-grass.jpg",
        "https://assets-au-01.kc-usercontent.com/ab37095e-a9cb-025f-8a0d-c6d89400e446/33e0f89e-e666-4630-bed8-be87558a858f/article-cat-and-dog-skin-conditions-common.jpg"
    ]
}'
```
