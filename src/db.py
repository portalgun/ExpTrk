import mysql.connector
import socket

class myDb:
    DBNAME="expTrk"
    TABLES=("obj", "version",
            "creator",
            "creator_alias",
            "creator_host",
            "execution",
            "tag",
            "obj_tag",
            "heir",
            "location",
            "param")

    def init(self,user,password,host="127.0.0.1",port=3306):
        self.host=host;
        self.user=user;
        self.password=password
        self.port=port
        self.output=""

        assert self.is_port_open(), "Host not connectable through given port"

        self.connect()

        if not self.is_database():
            self.create_db()
            self.create_all_tables()


        for t in self.TABLES:
            if not self.is_table(t):
                eval("self.create_" + t + "_table()")

## CHECKS
    def is_port_open(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        return sock.connect_ex((self.host,self.port))==0

    def is_database(self):
        str="""SELECT SCHEMA_NAME
            FROM INFORMATION_SCHEMA.SCHEMATA
            WHERE SCHEMA_NAME = '""" + self.DBNAME + """';"""

        self.execute(str)
        return self.cursor.rowcount > 0

    def is_table(self,tableName):
        str="""SELECT COUNT(*)
        FROM information_schema.tables
        WHERE table_schema = '""" + self.DBNAME + """'
        AND table_name = '""" + tableName + """';"""

        self.execute(str)
        return self.cursor.rowcount > 0

## INIT
    def connect(self):
        self.con=mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.DBNAME,
        )
        assert self.con.is_connected(), "Not able to connect"

        # XXX HANDLE SUCCESS FAILURE

    def create_all_tables(self):
        self.create_obj_table()
        self.create_seed_table()
        self.create_version_table()
        self.create_creator_table()
        self.create_aliases_table()
        self.create_host_table()
        self.create_executions_table()
        self.create_tag_table()
        self.create_heir_table()
        self.create_location_table()
        self.create_param_table()

    def create_db():
        str="""CREATE DATABASE """ + """'""" + self.DBNAME + """';"""
        self.execute(str)

    def create_user():
            str="""GRANT ALL PRIVILEGES ON '""" + self.DBNAME + """'.*
            TO '"""  + self.user  + """'@localhost
            IDENTIFIED BY '""" + self.password + """';"""
            self.execute(str)
            self.execute("FLUSH PRIVILEGES")


    def use():
        self.execute("USE " + self.DBNAME)

## UTIL
    def execute(self, cmd):
        try:
            with self.con.cursor(buffered=True) as self.cursor:
                self.cursor.execute(cmd)
        except:
            if self.con.is_connected():
                self.con.close()
            print(cmd)
            raise

    def print(self):
        for row in self.cursor:
            print(row)
        # XXX GET  OUTPUT


    def insert(self,tableName,*args):
        str="INSERT INTO '" + tableName + "' VALUES ("
        for x in args:
            str += x + ","
        str=str[:-1] + ")"
        self.execute(str)

    def select(self,tableName,keys,vals,ops,order=None,flds=None):

        if len(flds) > 0:
            str = ""
            for fld in flds:
                str += str + flds[i] + ", "
            str=str[:-1]
        else:
            str = "*"

        str="SELECT " + str + " FROM '" + tablename + "' "

        if len(keys) > 0:
            str += "WHERE "
            for i in range(len(keys)):
                str += keys[i] +  " " + eqs[i] + " " + vals[i] + " "
                if ops[i]:
                    str += + ops[i] + " "

        if order:
            str += "ORDER BY " + order

        self.execute(str)



##  TABLE
    def create_obj_table(self):
        str="""CREATE TABLE obj (
        id INT AUTO_INCREMENT PRIMARY KEY,
        type VARCHAR(10),
        name VARCHAR(20),
        created TIMESTAMP,
        creator INT,
        imported TIMESTAMP,
        importer INT,
        vers_id MEDIUMINT UNSIGNED,
        seed_id MEDIUMINT UNSIGNED
        );"""
        self.execute(str)


##  SEED

    def create_seed_table(self):
        str="""CREATE TABLE seed (
        id INT AUTO_INCREMENT PRIMARY KEY,
        human_id INT
        name VARCHAR(20),
        lib VARCHAR(10),
        type VARCHAR(10),
        hash VARCHAR(10),
        );"""
        self.execute(str)

##  VERSION
    def create_version_table(self):
        # VERSIONS
        str="""CREATE TABLE versions (
        id INT AUTO_INCREMENT PRIMARY KEY,
        type VARCHAR(10),
        hash VARCHAR(10),
        );"""
        self.execute(str)

##  CREATOR
    def create_creator_table(self):
        # CREATOR
        str="""CREATE TABLE creator (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(20)
        );"""
        self.execute(str)

##  CREATOR ALISES
    def create_creator_aliase_table(self):
        str="""CREATE TABLE creator_aliase (
        creator_id,
        name VARCHAR(20),
        );"""
        self.execute(str)

##  CREATOR HOSTS
    def create_creator_host_table(self):
        str="""CREATE TABLE creator_host (
        creator_id VARCHAR(20),
        user VARCHAR(20),
        hostname VARCHAR(20),
        );"""
        self.execute(str)

##  EXECUTIONS
    def create_execution_table(self):
        str="""CREATE TABLE execution (
        id INT AUTO_INCREMENT PRIMARY KEY,
        hostname VARCHAR(20),
        user VARCHAR(20),
        timestamp TIMESTAMP,
        );"""
        self.execute(str)

##  TAG
    def create_tag_table(self):
        str="""CREATE TABLE tag (
        obj_id INT,
        name VARCHAR(20),
        );"""
        self.execute(str)

##  OBJ-TAG
    def create_obj_tag_table(self):
        str="""CREATE TABLE obj_tags (
        obj_id INT,
        tag_id INT,
        );"""
        self.execute(str)

##  HEIR
    # HEIRARCHY
    def create_heir_table(self):
        str="""CREATE TABLE heir (
        par_obj_id INT
        chi_obj_id INT
        );"""
        self.execute(str)

##  LOCATION
    def create_location_table(self):
        str="""CREATE TABLE location (
        obj_id INT
        loc VARCHAR(256)
        );"""
        self.execute(str)

##  PARAM
    def create_param_table(self):
        str="""CREATE TABLE param (
        id INT AUTO_INCREMENT PRIMARY KEY,
        obj-id INT
        name
        );"""
        self.execute(str)

