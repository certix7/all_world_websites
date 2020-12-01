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
    print('we creat our database')
    # creating database
    db = sqlite3.connect('test.db')
    db.row_factory = sqlite3.Row
     # drop table
    db.execute('drop table if exists sites')
    comm=''' CREATE TABLE sites (link TEXT NOT NULL)'''
    #run the sql comand
    db.execute(comm)
    print("***************************")
    files=input(" pls put your file name :") or "data.txt"
    count=1
    with open(files,"r") as wordlist_file:
            for line in wordlist_file:
                test_url = line.strip()
                count+=1
                print(count)
                #add(test_url)
                db.execute(f'INSERT INTO sites (link)VALUES("{line}")')
    db.commit()
    print("******************************************")
    print ("wel done you scrape the planet sites now hero")
    print("****************************************************")



if __name__ == "__main__": main()











'''
    curser=db.execute('select * from sites')
    for row in curser:
        row=dict(row)
        print(row)

'''