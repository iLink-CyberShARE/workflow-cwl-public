# Pull ubuntu latest LTS image
FROM ubuntu:21.10

ENV DEBIAN_FRONTEND noninteractive

# Update the environment and perform apt installations
RUN apt-get update -y \
    && apt-get install -y python3 \
    && apt-get install -y mysql-server \
    && apt-get install -y python3-pip \
    && apt-get install -y python3-venv \
    && apt-get install -y libmysqlclient-dev \
    && apt-get install -y curl \
    # && yum install -y jq \
    && apt-get clean

# create a directory for app
WORKDIR /workflow-cwl

# Copy project directory into the container at /workflow-serializer
COPY  . /workflow-cwl

# Update pip and setup virtual python environment
RUN python3 -m pip --no-cache-dir install --user --upgrade pip \
    && python3 -m pip --no-cache-dir install --user virtualenv \
    && python3 -m venv env \
    && . env/bin/activate

# Install the dependencies
RUN python3 -m pip --no-cache-dir install -r requirements.txt
RUN python3 -m pip --no-cache-dir install cwlref-runner

# Expose port
EXPOSE 5004

# Production WSGI Server
CMD ["uwsgi", "app.ini"]