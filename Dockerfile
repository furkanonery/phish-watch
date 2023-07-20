FROM python:3.10

WORKDIR /app

COPY pyproject.toml poetry.lock /app/
COPY src /app/src

RUN pip3 install --upgrade pip
RUN pip3 install poetry==1.5.1
RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction --no-ansi

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]