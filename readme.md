# Word2vec API Server
This is a docker application to run a simple API service for the Google Word2Vec model.

Not production safe.

## Install

```
$ docker pull l226/word2vec_api
$ docker run -it word2vec_api
```

## Usage

```
$ curl http://localhost:8000/king/queen
> $COSINE_DISTANCE
```