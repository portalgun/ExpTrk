#pip install mysql-connector-python blinker
#
# CREATE DATABASE expTrk;
# CREATE USER expTrk;
# GRANT ALL PRIVILEGES ON expTrk.* TO 'expTrk'@localhost IDENTIFIED BY 'IL5aLOHeFzTGia';
# FLUSH PRIVILEGES;

from db import myDb
from controller import controller

def main():
    #listener=
    contr=controller()
    contr.send_msg("termUI","read")

if __name__ == "__main__":
    main()
