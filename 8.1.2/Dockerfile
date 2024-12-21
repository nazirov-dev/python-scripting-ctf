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
COPY firstScriptcheckScript.py /var/checker_files/firstScriptcheckScript.py

RUN chmod 777 /var/checker_files/firstScriptcheckScript.py && \
    chmod +x /var/checker_files/firstScriptcheckScript.py && \
    echo "python3 /var/checker_files/firstScriptcheckScript.py &" >> /home/haady/.bashrc && \
    chmod +x /home/haady/.bashrc

USER haady
WORKDIR /home/haady

CMD ["/bin/bash"]