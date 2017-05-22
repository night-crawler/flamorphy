FROM python:3-alpine

WORKDIR /application/flamorphy
ADD requirements.txt /application/flamorphy

RUN apk update && apk upgrade
RUN apk --update add --virtual build-dependencies build-base \
        && pip install pip -U && pip install wheel \
        && pip install -r requirements.txt \
        && apk del build-dependencies

ADD . /application/flamorphy
RUN mkdir /application/log && mkdir /application/run

RUN adduser -D -u 1000 flamorphy -h /application
RUN chown -hR flamorphy: /application

USER flamorphy
EXPOSE 1681

ENTRYPOINT ["python", "manage.py"]
CMD ["gunicorn"]
