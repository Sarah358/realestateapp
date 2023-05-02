FROM python:3.10.0-slim-buster

# SETUP WORKDIR
ENV APP_HOME=/app
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/staticfiles
WORKDIR $APP_HOME

# SETUP META DATA FOR IMAGE
LABEL maintainer = 'njerinjuguna358@gmail.com'
LABEL description = "Development image for real estate project"

# SETUP ENV VARIABLES
# prevents python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE 1    

# allows display of application in real time
ENV PYTHONUNBUFFERED 1

# INSTALL DEPENDENCIES (-Y ENSURES IT DOESNT STOP TO ASK FOR USER PROMPT)
RUN apt-get update \
  && apt-get install -y build-essential \
  && apt-get install -y libpq-dev \
  && apt-get install -y gettext \
  && apt-get -y install netcat gcc postgresql \
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

# update pip
RUN pip install pip

# install pipenv and dependencies
COPY Pipfile Pipfile.lock /app/
RUN pip install pipenv && pipenv install --system

# run entrypoint shell script
COPY ./docker/local/django/entrypoint /entrypoint
# convert any windows line index to linux line index
RUN sed -i 's/\r$//g' /entrypoint
# make entrypoint script executable
RUN chmod +x /entrypoint

# start shell script
COPY ./docker/local/django/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

COPY ./docker/local/django/celery/worker/start /start-celeryworker
RUN sed -i 's/\r$//g' /start-celeryworker
RUN chmod +x /start-celeryworker

COPY ./docker/local/django/celery/flower/start /start-flower
RUN sed -i 's/\r$//g' /start-flower
RUN chmod +x /start-flower

# directory for entrypoint
ENTRYPOINT [ "/entrypoint"]

