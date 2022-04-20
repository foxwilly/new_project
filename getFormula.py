#! /usr/bin/env python
__author__ = "Willy Fernandez"
__author_email__ = "wilferna@cisco.com"
__copyright__ = "Copyright (c) 2022 Cisco Systems, Inc."
__license__ = "MIT"
"""
Script to get the formulas from json files exported from Grafana
19-04-2022 include try to catch exception to consider the scenario when the panels without target
"""

import json
"""
import os
dashboards = os.popen(f"dir /B files").read()
# print(dashboards)
file1 = open('jsonFiles.txt', 'w')
file1.writelines("files/"+dashboards)
file1.close()

# Using readlines()
file1 = open('jsonFiles.txt', 'r')
Lines = file1.readlines()
for name in Lines:
  """
with open('files/AKRNOH1 - SYSTEM_SUMMARY_v1.0.06-1626717934059.json', 'r') as f:
  data = json.load(f)
  print(data['title'])
  # print(json.dumps(data['panels'][1]["title"], indent=4, sort_keys=True))
  for panel in data['panels']:
    print(panel["title"])
    try:
      for formula in panel['targets']:
        print(formula['target'])
    except:
        print("no target in this panel")
