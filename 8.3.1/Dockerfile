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
COPY forDictionarycheckScript.py /var/checker_files/forDictionarycheckScript.py
COPY start_checker.sh /var/checker_files/start_checker.sh
COPY forDictionary.py /home/haady/forDictionary.py

RUN chown haady:haady /var/checker_files/forDictionarycheckScript.py && \
    chmod 777 /var/checker_files/forDictionarycheckScript.py && \
    chmod +x /var/checker_files/start_checker.sh && \
    chown haady:haady /home/haady/forDictionary.py && \
    chmod 777 /home/haady/forDictionary.py && \
    echo '/var/checker_files/start_checker.sh' > /home/haady/.bashrc

USER haady
WORKDIR /home/haady

CMD ["/bin/bash"]

