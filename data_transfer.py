#import psycopg2
import time
import sqlite3

# vars
incremental_commit_size=10000   # number of rows
throttle_time=0         # seconds
conn = sqlite3.connect(database="db.sqlite3",check_same_thread=False)
#cur = conn.cursor()

#connectstr=psycopg2.connect(host="dc.kenmarkserver.com", port = 5437, database="traffic_database", user="laqshya", password="Laqshya@16373!")
#handle=sqlite3.connect(connectstr)
cursor=conn.cursor()
cursor2=conn.cursor()
sql="select maid_count from traffic_data_cities_cluster"
cursor.execute(sql)

while 1:

  output = cursor.fetchmany(incremental_commit_size)
  print(output)

  if not output:
    break
  for row in output:
    print(row)

    # update table
    sql="INSERT INTO traffic_data_npr_calculation(maid_count) values(%d)"%(row)
    #sql = "update traffic_data_npr_calculation set maid_count= cast(maid_count) where maid_count = %s" 
    cursor2.execute(sql)#,([row[0]]))

  #commit, invoked every incremental commit size
  conn.commit()
  time.sleep(throttle_time)

conn.commit()

