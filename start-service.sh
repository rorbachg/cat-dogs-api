docker build -t cats-dogs-api .
docker build -t cats-dogs-api-test -f test-Dockerfile .
# docker run --name cats-dogs-api-container -p 80:80 cats-dogs-api
