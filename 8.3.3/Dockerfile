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
COPY nameAgecheckScript.py /var/checker_files/nameAgecheckScript.py
COPY start_checker.sh /var/checker_files/start_checker.sh
COPY nameAge.py /home/haady/nameAge.py

RUN chown -R haady:haady /var/checker_files && \
    chmod -R 777 /var/checker_files && \
    chmod +x /var/checker_files/start_checker.sh && \
    chown -R haady:haady /home/haady && \
    chmod -R 777 /home/haady && \
    echo '/var/checker_files/start_checker.sh' > /home/haady/.bashrc

USER haady
WORKDIR /home/haady

CMD ["/bin/bash"]

