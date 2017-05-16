FROM debian:stretch
LABEL maintainer "www@force.fm"

ENV FLAMORPHY_VERSION '0.1.0'

RUN apt-get update
RUN apt-get install -y python3 python3-venv
RUN pyvenv /venv

# activate venv
ENV PATH /venv/bin:$PATH

# Copy only the requirements file, to avoid rebuilding on every file change
COPY requirements.txt ./
# separate bdist_wheel install
RUN pip install wheel
RUN pip install -r requirements.txt

RUN mkdir /venv/run; mkdir /venv/log

COPY . /venv/application/
WORKDIR /venv/application

RUN useradd flamorphy -d /venv/application
RUN chown -hR flamorphy: /venv/run; chown -hR flamorphy: /venv/log; chown -hR flamorphy: /venv/application

USER flamorphy
EXPOSE 1681

#CMD ["gunicorn", "--config", "./gunicorn_release.py", "wsgi:application"]
ENTRYPOINT ["python", "manage.py"]
CMD ["gunicorn"]
