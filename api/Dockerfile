FROM python:3-slim

WORKDIR /srv/api

COPY ./requirements.txt ./
RUN pip install -r ./requirements.txt \
    && rm requirements.txt
    
COPY ./spec ./spec
COPY ./src ./src
COPY ./gunicorn.conf.py ./

ENTRYPOINT ["gunicorn", "-c", "./gunicorn.conf.py", "src:app"]
