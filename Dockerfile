FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /movies
WORKDIR /movies/
COPY requirements.txt /movies/
RUN pip install -r requirements.txt 
ARG IMDB_KEY
ENV IMDB_KEY=4c56463f39mshc83a0842d95dcf2p1a7364jsn1f41a82a0394
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
COPY . /movies/