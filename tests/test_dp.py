import unittest
import myDb


# CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'IL5aLOHeFzTGia';
# CREATE DATABASE expTrk;
# CREATE USER expTrk;
# GRANT ALL PRIVILEGES ON expTrk.* TO 'expTrk'@localhost IDENTIFIED BY 'IL5aLOHeFzTGia';
# FLUSH PRIVILEGES;


db=myDb("expTrk","IL5aLOHeFzTGia")
