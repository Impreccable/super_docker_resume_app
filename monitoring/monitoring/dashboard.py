import streamlit as st
import psycopg2
import os


"Statistics about our visitors"

#st.write("db ujsername, st.secrets.connections.postgresql.username")


#initiliaze connection with db
if os.getenv("CONTAINER_ON"):
    conn = st.connection("postgresql_container", type= "sql")

else :
    conn = st.connection("postgresql", type= "sql") 



# Perform query.
df = conn.query('SELECT * FROM contact;')

# Print results.
#for row in df.itertuples():
    #st.write(f"{row} ")

st.table(df)