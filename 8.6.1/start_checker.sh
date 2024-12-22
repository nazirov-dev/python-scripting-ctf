#!/bin/bash

nohup python3 /var/server_listeners/server_6666.py >/dev/null 2>&1 &
nohup python3 /var/server_listeners/server_7777.py >/dev/null 2>&1 &
nohup python3 /var/server_listeners/server_8888.py >/dev/null 2>&1 &
