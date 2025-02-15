#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import telnetlib
import time

from hackerutils import sh

COFFEE_MACHINE_ADDR = '10.10.42.42'
COFFEE_MACHINE_PASS = '1234'
COFFEE_MACHINE_PROM = 'Password: '


def main():
    # Exit early if no sessions with my_username are found.
    if not any(s.startswith(b'my_username') for s in sh('who').split(b'\n')):
        return

    time.sleep(17) # sleep system for 17 seconds

    conn = telnetlib.Telnet(host=COFFEE_MACHINE_ADDR)  #creating the connection
    conn.open()
    conn.expect([COFFEE_MACHINE_PROM])
    conn.write(COFFEE_MACHINE_PASS)

    conn.write('sys brew')
    time.sleep(64)    # sleep system for 16 seconds

    conn.write('sys pour')
    conn.close()     # closing the connection


if __name__ == '__main__':  #check__name__ is equal to __main__ or  not.
    main()
