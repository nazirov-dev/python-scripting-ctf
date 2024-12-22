FROM ubuntu:20.04

# Set noninteractive frontend to avoid tzdata prompt
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    nano \
    vim \
    iproute2 \
    net-tools \
    apache2 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN useradd -m -s /bin/bash haady && \
    echo "haady:haady" | chpasswd

RUN mkdir /home/haady/webDownloader
COPY webDownloader.py /home/haady/webDownloader/webDownloader.py
COPY webDownloadercheckScript.py /home/haady/webDownloader/webDownloadercheckScript.py

# Set up Apache directories and permissions
RUN chown -R haady:haady /home/haady && \
    chown -R www-data:www-data /var/www/html && \
    mkdir -p /var/run/apache2 && \
    mkdir -p /var/lock/apache2 && \
    mkdir -p /var/log/apache2 && \
    chown -R www-data:www-data /var/run/apache2 && \
    chown -R www-data:www-data /var/lock/apache2 && \
    chown -R www-data:www-data /var/log/apache2

# Create startup script
RUN echo '#!/bin/bash\nservice apache2 start\nexec "$@"' > /start.sh && \
    chmod +x /start.sh

# Add ServerName directive to suppress FQDN warning
RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf

# Switch to root for Apache startup
USER root
WORKDIR /home/haady

CMD ["/start.sh", "/bin/bash"]