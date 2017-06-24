# Word2vec API Server
This is a docker application to run a simple API service for the Google Word2Vec model.

Not production safe. Might be broken.

## Install

```
$ docker pull lfriescozero/word2vec_api
$ docker run -it word2vec_api
```

## Usage

```
$ curl http://localhost:8000/sweden/norway
> 0.760124
```