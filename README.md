# phish-watch
Defines a surveillance and monitoring system against phishing attacks.

### Running the Server

1. Navigate to the `phish-watch` directory:

    ```
    cd phish-watch
    ```

2. To run the server, execute the following command:

    ```
    poetry run uvicorn src.main:app --reload
    ```

### Starting Celery Worker and Beat

1. Navigate to the `tasks` directory:

    ```
    cd phish-watch/src/tasks
    ```

2. To start the Celery Worker, run the following command:

    ```
    celery -A celery_config.celery_app worker --loglevel=info
    ```

3. To start the Celery Beat, run the following command:

    ```
    celery -A celery_config.celery_app beat --loglevel=info
    ```
