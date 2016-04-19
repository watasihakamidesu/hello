from multiprocessing import Process, Pipe

def send(conn):
    conn.send("Hello World")
    conn.close()

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=send, args=(child_conn,))
    p.start()
    print parent_conn.recv()
