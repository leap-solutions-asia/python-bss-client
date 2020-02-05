FROM python:3.8-slim
WORKDIR /work
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y git && \
    apt-get clean -y
RUN pip install --upgrade pip && \
    pip install git+https://github.com/leap-solutions-asia/python-bss-client.git
ENTRYPOINT [ "bss" ]
