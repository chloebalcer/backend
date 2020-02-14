FROM python:3.7.4
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install --upgrade pip -r requirements.txt
COPY scripts/start*.sh /
ADD . /code/
CMD ["sh", "/start_prod.sh"]