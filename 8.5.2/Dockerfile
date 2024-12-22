FROM ubuntu:20.04

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    nano \
    vim \
    iproute2 \
    net-tools \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN useradd -m -s /bin/bash haady && \
    echo "haady:haady" | chpasswd

RUN mkdir /home/haady/webDownloader
COPY webDownloader.py /home/haady/webDownloader/webDownloader.py
COPY webDownloadercheckScript.py /home/haady/webDownloader/webDownloadercheckScript.py

RUN chown -R haady:haady /home/haady

USER haady
WORKDIR /home/haady

CMD ["/bin/bash"]