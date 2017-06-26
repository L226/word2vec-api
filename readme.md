# Word2vec API Server
This is a docker application to run a simple API service for the Google Word2Vec model.

Not production safe.

## Install

```
$ docker pull lfriescozero/word2vec-api
$ docker run -it lfriescozero/word2vec-api
```

## Usage

Currently only provides cosine distance between 2 words: 

```
$ curl http://localhost:8000/sweden/norway
> 0.6274740358867263

$ curl http://localhost:8000/king/queen
> 0.6510956835386661

$ curl http://localhost:8000/man/woman
> 0.7664012230995352
```

Returns null if word not found in model vocabulary.