CREATE A TABLE
import mysql.connector
demodb = mysql.connector.connect(host="localhost", user="root", passwd="computer",
database="EDUCATION")
democursor=demodb.cursor( )
democursor.execute("CREATE TABLE STUDENT (admn_no int primary key, sname
varchar(30), gender char(1), DOB date, stream varchar(15), marks float(4,2))")
INSERT THE DATA
import mysql.connector
demodb = mysql.connector.connect(host="localhost", user="root", passwd="computer",
database="EDUCATION")
democursor=demodb.cursor( )
democursor.execute("insert into student values (%s, %s, %s, %s, %s, %s)", (1245, 'Arush',
'M', '2003-10-04', 'science', 67.34))

import mysql.connector
demodb = mysql.connector.connect(host="localhost", user="root", passwd="computer",
database="EDUCATION")
democursor=demodb.cursor( )
democursor.execute("delete from student where admn_no=1356")
demodb.commit( ) demodb.commit( )

FETCH THE DATA

import mysql.connector
demodb = mysql.connector.connect(host="localhost", user="root", passwd="computer",
database="EDUCATION")
democursor=demodb.cursor( )
democursor.execute("select * from student")
for i in democursor:
print(i) 
UPDATE THE RECORD
import mysql.connector
demodb = mysql.connector.connect(host="localhost", user="root", passwd="computer",
database="EDUCATION")
democursor=demodb.cursor( )
democursor.execute("update student set marks=55.68 where admn_no=1356")
demodb.commit( ) 
