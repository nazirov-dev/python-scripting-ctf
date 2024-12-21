FROM ubuntu:20.04

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    nano \
    vim \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN useradd -m -s /bin/bash haady && \
    echo "haady:haady" | chpasswd

RUN mkdir /var/checker_files
COPY urlSlicecheckScript.py /var/checker_files/urlSlicecheckScript.py
COPY start_checker.sh /var/checker_files/start_checker.sh
COPY urlSlice.py /home/haady/urlSlice.py

RUN chmod 777 /var/checker_files/urlSlicecheckScript.py && \
    chmod +x /var/checker_files/urlSlicecheckScript.py && \
    chmod +x /var/checker_files/start_checker.sh && \
    echo "/var/checker_files/start_checker.sh" >> /home/haady/.bashrc

USER haady
WORKDIR /home/haady

CMD ["/bin/bash"]
