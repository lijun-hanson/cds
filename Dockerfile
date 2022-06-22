FROM python:3.8-buster

WORKDIR /opt/workspace

ADD . $WORKDIR
RUN pip3 install pip --upgrade
RUN pip3 install --no-input -r requirements.txt

ENTRYPOINT ["flask", "run"]
