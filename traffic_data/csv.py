import psycopg2 #import the postgres library

#connect to the database
conn = psycopg2.connect(host="dc.kenmarkserver.com", port = 5437, database="traffic_database", user="laqshya", password="Laqshya@16373!")
#create a cursor object 
#cursor object is used to interact with the database
cur = conn.cursor()

#create table with same headers as csv file
# cur.execute("CREATE TABLE IF NOT EXISTS test(**** text, **** float, **** float, **** 
# text)")

#open the csv file using python standard file I/O
#copy file into the table just created 
with open('tier_label_days_vehicle_perc.csv', 'r') as f:
    next(f) # Skip the header row.
    #f , <database name>, Comma-Seperated
    cur.copy_from(f, 'traffic_data_model_class', sep=',')
    #Commit Changes
    conn.commit()
    #Close connection
    conn.close()