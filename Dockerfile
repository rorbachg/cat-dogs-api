FROM ubuntu:22.04

WORKDIR /opt/ml/code

COPY model /opt/ml/model
COPY v1 /opt/ml/code/v1
COPY requirements.txt /opt/ml/code/
COPY main.py /opt/ml/code/

RUN apt-get update
RUN apt-get install -y python3.10
RUN apt-get install -y python3-pip
RUN pip3 install -r /opt/ml/code/requirements.txt

ENV MODEL_PATH /opt/ml/model/

ENTRYPOINT [ "uvicorn" ]
CMD ["main:app", "--host", "0.0.0.0", "--port", "80", "--workers", "1"]
