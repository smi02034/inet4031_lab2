#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()
# To get rid of the commented-out line at the end of fileprocessor.input
lines.pop()

for line in lines:
    userName = line[0:5]

    userPass = line[6:15]

    userID = line[16:17]

    groupID = line[18:19]

    print('The user ' + userName + ' has a password of ' + userPass + \
        ' and a userid of ' + userID + ' and a groupid of ' + groupID)
