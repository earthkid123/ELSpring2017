#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sqlite3 as lite
import sys
import time

def getTimee():
        con=lite.connect('testTime.db')
        with con:
                cur=con.cursor()
                cur.execute("SELECT * FROM time")
                rows=cur.fetchall()
                for row in rows:
                        print(row)
print(getTimee())
