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

RUN mkdir /home/haady/import
COPY importTest.py /home/haady/import/importTest.py
COPY importMe.py /home/haady/import/importMe.py

RUN chown -R haady:haady /home/haady

USER haady
WORKDIR /home/haady

CMD ["/bin/bash"]