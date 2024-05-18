FROM python:3.10-slim-bullseye

# Add user
RUN useradd --create-home crm-fervan && \
    chown -R crm-fervan /home/crm-fervan && \
    usermod -aG sudo crm-fervan && \
    find /usr/local/lib -type d -exec chmod 777 {} \; && \
    find /usr/local/bin -type d -exec chmod 777 {} \;

RUN groupadd docker && \
    usermod -aG docker crm-fervan

# Release File Error
# https://stackoverflow.com/questions/63526272/release-file-is-not-valid-yet-docker
RUN echo "Acquire::Check-Valid-Until \"false\";\nAcquire::Check-Date \"false\";" | cat > /etc/apt/apt.conf.d/10no--check-valid-until

# System packages
RUN apt update -q && yes | apt install -q gnupg vim unixodbc-dev build-essential \
    curl python3-dev libboost-all-dev libpq-dev python3-gi sudo git software-properties-common
ENV PIP_NO_CACHE_DIR=1
RUN pip install --upgrade cffi

# Fix for old SQL Servers still using TLS < 1.2
RUN chmod +rwx /usr/lib/ssl/openssl.cnf && \
    sed -i 's/SECLEVEL=2/SECLEVEL=1/g' /usr/lib/ssl/openssl.cnf

COPY app-docker/odbcinst.ini /etc

# Install necessary networking tools
RUN apt-get update && apt-get install -y \
    iputils-ping \
    net-tools \
    telnet \
    nmap

# This one's needed for the SAP RFC connector. 
# It must be installed here as the SAP package does not define its dependencies, 
# so `pip install pyrfc` breaks if all deps are not already present.
RUN pip install cython==0.29.24

# Python env
WORKDIR /code
COPY requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .
#RUN pip install .

VOLUME /home/crm-fervan

# Workdir
ENV USER crm-fervan
ENV HOME="/home/$USER"

# Python stuff
ENV PYTHONPATH=/home/crm-fervan

WORKDIR ${HOME}

USER ${USER}

# Create the .ssh directory and known_hosts file
RUN mkdir -p /home/crm-fervan/.ssh && touch /home/crm-fervan/.ssh/known_hosts

# Run the ssh-keyscan command to add the host key to known_hosts
RUN ssh-keyscan u371377.your-storagebox.de >> ~/.ssh/known_hosts

CMD ["sleep", "infinity"]