#!/usr/bin/env python
# coding: utf-8



from datetime import datetime
import json
import random
import os
import sys
import time
import urllib.parse
import pandas as pd


def read():
    data_complete= pd.read_csv('creditcard.csv')
    data = data_complete.iloc[:50,:]
    for x in range(5):
        time.sleep(1.0)
        val=data.iloc[x,:]
        json=val.to_json ()
        print(json)
        sys.stdout.write(json)
        sys.stdout.flush()
read()










