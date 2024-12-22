FROM ubuntu:20.04

# Set noninteractive frontend to avoid tzdata prompt
ENV DEBIAN_FRONTEND=noninteractive

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
    echo "haady:haady" | chpasswd && \
    mkdir /var/server_listeners


COPY server_6666.py /var/server_listeners/server_6666.py
COPY server_7777.py /var/server_listeners/server_7777.py
COPY server_8888.py /var/server_listeners/server_8888.py


COPY start_checker.sh /var/server_listeners/start_checker.sh
RUN chown -R haady:haady /var/server_listeners/start_checker.sh && \
    chmod +x /var/server_listeners/start_checker.sh && \
    echo '/var/server_listeners/start_checker.sh' >> /home/haady/.bashrc && \
    pip3 install socket requests && \
    chown -R haady:haady /var/server_listeners/server_6666.py && \
    chown -R haady:haady /var/server_listeners/server_7777.py && \
    chown -R haady:haady /var/server_listeners/server_8888.py && \
    chown -R haady:haady /home/haady

WORKDIR /home/haady
USER haady

CMD ["/bin/bash"]






