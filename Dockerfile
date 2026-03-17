
FROM python:3.12-slim


WORKDIR /code


COPY ./requirements.txt /code/requirements.txt
COPY ./model.pkl /code/app/
COPY ./model.pkl /code/


RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt


COPY ./app /code/app


CMD ["fastapi", "run", "app/main.py", "--port", "80"]