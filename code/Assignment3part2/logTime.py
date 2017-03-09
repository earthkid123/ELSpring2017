#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import time
import sqlite3 as lite
import sys

def logTime():
        con=lite.connect('testTime.db')
        xTime=time.strftime("%H:%M:%S")
        xDate = time.strftime("%d/%m/%y")
        cur=con.cursor()
        cur.execute("INSERT INTO time VALUES (?,?)", (xTime,xDate))
        con.commit()
        con.close()
print("Time logged")
