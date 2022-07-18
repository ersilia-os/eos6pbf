FROM bentoml/model-server:0.11.0-py37
MAINTAINER ersilia

RUN conda install -c conda-forge selfies

WORKDIR /repo
COPY . /repo
