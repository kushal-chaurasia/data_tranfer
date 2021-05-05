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

  if not output:
    break
  for row in output:

    # update table
    sql="update traffic_data_npr_calculation set maid_count= " #set latdouble = cast(latvarchar as double precision) where tKey = %s
    cursor2.execute(sql,([row[0]]))

  #commit, invoked every incremental commit size
  handle.commit()
  time.sleep(throttle_time)

handle.commit()

