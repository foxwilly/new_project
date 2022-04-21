#!/usr/bin/env python
"""
Copyright Cisco Systems
2021 by Will Fernandez
Running in Python (2.7)
python import_carbon_data.py metric_path value timestamp

This pice of code is to send  data to Graphite.
Once Graphite server setup is ready, with Carbon running/collecting, it was needed to send it data for graphing.

To send data, a socket needs to be create hence stablish a connection with graphite/carbon server and send a message (string) in the format: (metric_path value timestamp)
        - metric_path: arbitrary namespace containing substrings delimited by dots. The most general name is at the left and the most specific is at the right.
        - value: numeric value to store.
        - timestamp: with the format YYYY-MM-DD 23:00:00

"""

import platform
import socket
import time
import argparse

CARBON_SERVER = '0.0.0.0'
CARBON_PORT = 2013
DELAY = 15  # secs


def get_message():
    parser = argparse.ArgumentParser()
    parser.add_argument('metric_path')
    parser.add_argument('value')
    parser.add_argument('timestamp')
    args = parser.parse_args()
    pattern = '%Y-%m-%d_%H:%M:%S'
    timestamp = int(time.mktime(time.strptime(args.timestamp, pattern)))
    '''timestamp = int(time.time())'''
    message = '%s %s %d\n' % (args.metric_path, args.value, timestamp)
    return message


def send_msg(message):
    print 'sending message:\n%s' % message
    sock = socket.socket()
    sock.connect((CARBON_SERVER, CARBON_PORT))
    sock.sendall(message)
    sock.close()


if __name__ == '__main__':
    '''node = platform.node().replace('.', '-')
    while True:'''
    message = get_message()
    send_msg(message)
    '''time.sleep(DELAY)'''
