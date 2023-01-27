#!/usr/bin/env python3

f = open("fileprocessor.input", "r")
for i in range(3):
    userName = f.read(5)
    f.read(1)

    userPass = f.read(9)
    f.read(1)

    userID = f.read(1)
    f.read(1)

    groupID = f.read(1)
    f.read(1)

    print('The user ' + userName + ' has a password of ' + userPass + \
        ' and a userid of ' + userID + ' and a groupid of ' + groupID)
