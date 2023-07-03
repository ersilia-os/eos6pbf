FROM bentoml/model-server:0.11.0-py37
MAINTAINER ersilia

RUN pip install selfies

WORKDIR /repo
COPY . /repo
