import cx_Oracle

conn_str = “user/password@host:port/service”
with cx_Oracle.connect(conn_str) as conn:
    with conn.cursor() as cur:
        cur.executemany("INSERT INTO vip_customers(customer_id) VALUES (:1)", vipIds)

