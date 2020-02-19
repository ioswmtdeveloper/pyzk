# Get attendances (will return list of Attendance object)



# -*- coding: utf-8 -*-
import os
import sys

CWD = os.path.dirname(os.path.realpath(__file__))
ROOT_DIR = os.path.dirname(CWD)
sys.path.append(ROOT_DIR)

from zk import ZK, const


conn = None
zk = ZK('192.168.1.201', port=4370, timeout=5, password=0)
try:
    conn = zk.connect()
    conn.unlock(7)
except Exception as e:
    print ("Process terminate : {}".format(e))
finally:
    if conn:
        conn.disconnect()
