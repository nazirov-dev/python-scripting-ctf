# Unified Dockerfile for Python Scripting CTF
FROM ubuntu:20.04

# Set noninteractive frontend to avoid tzdata prompt
ENV DEBIAN_FRONTEND=noninteractive

# Install all required packages
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    nano \
    vim \
    iproute2 \
    net-tools \
    apache2 \
    cron \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Create user and set password
RUN useradd -m -s /bin/bash haady && \
    echo "haady:haady" | chpasswd

# Create necessary directories
RUN mkdir -p /var/server_listeners && \
    mkdir -p /var/checker_files && \
    mkdir -p /var/www/html/images && \
    mkdir -p /home/haady/import && \
    mkdir -p /home/haady/flag

# Copy all server files
COPY 8.6.1/server_6666.py /var/server_listeners/
COPY 8.6.1/server_7777.py /var/server_listeners/
COPY 8.6.1/server_8888.py /var/server_listeners/

# Copy all Python challenge files
COPY 8.1.2/firstScriptcheckScript.py /var/checker_files/
COPY 8.1.5/urlSlice.py /home/haady/
COPY 8.1.5/urlSlicecheckScript.py /var/checker_files/
COPY 8.1.8/booleanTest.py /home/haady/
COPY 8.1.8/booleanTestcheckScript.py /var/checker_files/
COPY 8.1.9/typeCasting.py /home/haady/
COPY 8.1.9/typeCastingcheckScript.py /var/checker_files/
COPY 8.2.1/createListcheckScript.py /var/checker_files/
COPY 8.3.1/forDictionary.py /home/haady/
COPY 8.3.1/forDictionarycheckScript.py /var/checker_files/
COPY 8.3.3/nameAge.py /home/haady/
COPY 8.3.3/nameAgecheckScript.py /var/checker_files/
COPY 8.5.1/importTest.py /home/haady/import/
COPY 8.5.1/importMe.py /home/haady/import/
COPY 8.5.2/webDownloader.py /home/haady/
COPY 8.5.2/webDownloadercheckScript.py /var/checker_files/

# Copy web content
COPY 8.5.2/images/* /var/www/html/images/
COPY 8.5.2/index.html /var/www/html/

# Copy and configure start checker script
COPY 8.6.1/start_checker.sh /var/checker_files/
RUN chmod +x /var/checker_files/start_checker.sh

# Set up Apache configurations
RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf && \
    chown -R www-data:www-data /var/www/html && \
    chown -R www-data:www-data /var/run/apache2 && \
    chown -R www-data:www-data /var/lock/apache2 && \
    chown -R www-data:www-data /var/log/apache2

# Set proper permissions
RUN chown -R haady:haady /home/haady && \
    chown -R haady:haady /var/server_listeners && \
    chown -R haady:haady /var/checker_files && \
    chmod -R 755 /var/checker_files/*.py && \
    chmod -R 755 /var/server_listeners/*.py && \
    chmod -R 755 /home/haady/*.py

# Install Python dependencies
RUN pip3 install requests

# Create startup script
RUN echo '#!/bin/bash\n\
service apache2 start\n\
/var/checker_files/start_checker.sh\n\
python3 /var/server_listeners/server_6666.py &\n\
python3 /var/server_listeners/server_7777.py &\n\
python3 /var/server_listeners/server_8888.py &\n\
clear\n\
exec "$@"' > /start.sh && \
    chmod +x /start.sh

# Add checker script to user's startup
RUN echo '/var/checker_files/start_checker.sh' >> /home/haady/.bashrc

WORKDIR /home/haady
USER haady

# Switch back to root for startup (needed for Apache and servers)
USER root
CMD ["/start.sh", "/bin/bash"]
