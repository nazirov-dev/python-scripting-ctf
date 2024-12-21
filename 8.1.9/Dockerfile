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
COPY typeCastingcheckScript.py /var/checker_files/typeCastingcheckScript.py
COPY start_checker.sh /var/checker_files/start_checker.sh
COPY typeCasting.py /home/haady/typeCasting.py

RUN chown haady:haady /home/haady/typeCasting.py && \
    chmod 777 /home/haady/typeCasting.py && \
    chmod +x /var/checker_files/start_checker.sh && \
    chmod +x /var/checker_files/typeCastingcheckScript.py && \
    echo "echo /var/checker_files/start_checker.sh" >> /home/haady/.bashrc

USER haady
WORKDIR /home/haady

CMD ["/bin/bash"]

