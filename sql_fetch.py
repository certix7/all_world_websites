#user/bin/python3

# Console colors
bg ='' # '\033[44m'  # gray
W = bg+'\033[0m'  # white (normal)
R = bg+'\033[31m'  # red
G = bg+'\033[32m'  # green
O = bg+'\033[33m'  # orange
B = bg+'\033[34m'  # blue
P = bg+'\033[35m'  # purple
C = bg+'\033[36m'  # cyan
GR = bg+'\033[37m'  # gray

GHT = G+'''
        +=========================================+
        |..........'''+O+'''chalange number [4] '''+G+'''...........|
        +-----------------------------------------+
        |'''+C+'''#Author: AHMED _NASER_Youssef'''+G+'''            |
        |'''+C+'''#Contact: youtube.com/c/certstars'''+G+'''        |
        |'''+C+'''#Date: 12/03/2020'''+G+'''                        |
        |'''+C+'''#This tool is made for pentesting. '''+G+'''      |
        |'''+C+'''#Changing the Code of this tool       '''+G+'''   |
        |'''+C+'''Won't made you the coder ^_^ !!!'''+G+'''         |
        |'''+C+'''#Respect Coderz ^_^           '''+G+'''           |
        |'''+C+'''#I take no responsibilities for the '''+G+'''     |
        |'''+C+''' use of this program !       '''+G+'''            |
        +=========================================+
        |..........'''+O+'''-----Cert Stars -----'''+G+'''..........|
        +-----------------------------------------+
'''+W
print(GHT)

import sqlite3

def main():
    print('---------------------------')
    print()
    put=input("put your search patren :")
    # creating database
    db = sqlite3.connect('test.db')
    db.row_factory = sqlite3.Row

    curser=db.execute("SELECT * FROM sites WHERE link LIKE '%{0}%'".format(put))
    for row in curser:
        row=dict(row)
        print(row['link'],end="")

    print('---------------------------')
    print()



if __name__ == "__main__": main()







'''
    curser=db.execute('select * from sites')
    for row in curser:
        row=dict(row)
        print(row)

'''