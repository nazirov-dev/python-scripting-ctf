FROM ubuntu:20.04

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
    echo "haady:haady" | chpasswd && \
    echo 'haady ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers && \
    echo 'root:haady' | chpasswd

RUN mkdir /var/checker_files

# CTF 8.1.2
COPY 8.1.2/firstScriptcheckScript.py /var/checker_files/firstScriptcheckScript.py

# CTF 8.1.5
COPY 8.1.5/urlSlicecheckScript.py /var/checker_files/urlSlicecheckScript.py
COPY 8.1.5/urlSlice.py /home/haady/urlSlice.py

#CTF 8.1.8
COPY 8.1.8/booleanTestcheckScript.py /var/checker_files/booleanTestcheckScript.py
COPY 8.1.8/booleanTest.py /home/haady/booleanTest.py

#CTF 8.1.9
COPY 8.1.9/typeCastingcheckScript.py /var/checker_files/typeCastingcheckScript.py
COPY 8.1.9/typeCasting.py /home/haady/typeCasting.py

#CTF 8.2.1
COPY 8.2.1/createListcheckScript.py /var/checker_files/createListcheckScript.py
COPY 8.2.1/createList.py /home/haady/createList.py

#CTF 8.3.1
COPY 8.3.1/forDictionarycheckScript.py /var/checker_files/forDictionarycheckScript.py
COPY 8.3.1/forDictionary.py /home/haady/forDictionary.py

#CTF 8.3.3
COPY 8.3.3/nameAgecheckScript.py /var/checker_files/nameAgecheckScript.py
COPY 8.3.3/nameAge.py /home/haady/nameAge.py

#CTF 8.5.1
RUN mkdir /home/haady/import
COPY 8.5.1/importTest.py /home/haady/import/importTest.py
COPY 8.5.1/importMe.py /home/haady/import/importMe.py

#CTF 8.5.2
COPY 8.5.2/webDownloader.py /home/haady/webDownloader.py
COPY 8.5.2/webDownloadercheckScript.py /var/checker_files/webDownloadercheckScript.py


RUN chown -R www-data:www-data /var/www/html && \
    mkdir -p /var/run/apache2 && \
    mkdir -p /var/lock/apache2 && \
    mkdir -p /var/log/apache2 && \
    mkdir -p /var/www/html/images

COPY 8.5.2/images/* /var/www/html/images/
COPY 8.5.2/index.html /var/www/html/index.html

RUN chown -R www-data:www-data /var/run/apache2 && \
    chown -R www-data:www-data /var/lock/apache2 && \
    chown -R www-data:www-data /var/log/apache2 && \
    chown -R www-data:www-data /var/www/html/images

# Add ServerName directive to suppress FQDN warning
RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf

RUN pip3 install requests

# Create startup script
RUN echo '#!/bin/bash\nservice apache2 start\n/var/checker_files/start_checker_files.sh\nclear\nsu haady\nexec "$@"' > /start.sh && \
    chmod +x /start.sh

#CTF 8.6.1
COPY 8.6.1/server_6666.py /var/checker_files/server_6666.py
COPY 8.6.1/server_7777.py /var/checker_files/server_7777.py
COPY 8.6.1/server_8888.py /var/checker_files/server_8888.py

#Copy checker files starter
COPY start_checker_files.sh /var/checker_files/start_checker_files.sh

# Set permissions for checker files
RUN chmod +x /var/checker_files/* && \
    chown -R root:root /var/checker_files/*

#Set permissions for CTF files
RUN chown -R haady:haady /home/haady/* && \
    chmod -R 644 /home/haady/*.py && \
    chown -R haady:haady /home/haady

USER root
WORKDIR /home/haady
RUN echo "/start.sh" >> /home/haady/.bashrc
CMD ["/bin/bash"]