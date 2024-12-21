FROM ubuntu:20.04

RUN apt-get update && apt-get install -y \
    python3 \
    && bash \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN useradd -m -s /bin/bash haady && \
    echo "haady:haady" | chpasswd
RUN mkdir /var/checker_files
COPY firstScriptcheckScript.py /var/checker_files/firstScriptcheckScript.py

RUN chmod 777 /var/checker_files/firstScriptcheckScript.py && \
    python3 /var/checker_files/firstScriptcheckScript.py

USER haady
WORKDIR /home/haady

CMD ["/bin/bash"]