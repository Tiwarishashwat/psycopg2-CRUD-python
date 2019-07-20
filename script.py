import psycopg2
def create_table():
    conn=psycopg2.connect("dbname='shashwat' user='postgres' password='Stiwari1999' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("create table IF NOT EXISTS store(item TEXT,quantity INTEGER,price REAL)")
    cur.execute("insert into store values('wine glass',8,10.5)")
    conn.commit()
    conn.close()
def insert_data(item,quantity,price):
    conn=psycopg2.connect("dbname='shashwat' user='postgres' password='Stiwari1999' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("insert into store values(%s,%s,%s)", (item,quantity,price))
    conn.commit()
    conn.close()
insert_data("water glass",8,98)
def delete_data(item):
    conn=psycopg2.connect("dbname='shashwat' user='postgres' password='Stiwari1999' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("delete from store where item=%s",(item,))
    conn.commit()
    conn.close()
delete_data("water glass")
def update_data(quantity,price,item):
    conn=psycopg2.connect("dbname='shashwat' user='postgres' password='Stiwari1999' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("update store set quantity=%s,price=%s where item=%s",(quantity,price,item))
    conn.commit()
    conn.close()
update_data(11,6,"wine glass")
def view():
    conn=psycopg2.connect("dbname='shashwat' user='postgres' password='Stiwari1999' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("select * from store")
    rows=cur.fetchall()
    conn.close()
    return rows
print(view())
create_table()
