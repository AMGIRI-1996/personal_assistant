FROM ubuntu:20.04
ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install --no-install-recommends -y \
    python3.8 python3-pip 

COPY ./src ./src
COPY ./requirements.txt ./requirements.txt
RUN python3 -m pip install -r requirements.txt 

EXPOSE ${PORT}
CMD python3 src/main.py
