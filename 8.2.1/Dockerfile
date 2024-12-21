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
COPY createListcheckScript.py /var/checker_files/createListcheckScript.py
COPY start_checker.sh /var/checker_files/start_checker.sh
COPY createList.py /home/haady/createList.py

RUN chown haady:haady /home/haady/createList.py && \
    chmod 777 /home/haady/createList.py && \
    chmod +x /var/checker_files/start_checker.sh && \
    chmod +x /var/checker_files/createListcheckScript.py && \
    echo '/var/checker_files/start_checker.sh' >> /home/haady/.bashrc

USER haady
WORKDIR /home/haady

CMD ["/bin/bash"]