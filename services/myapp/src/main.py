import socket, os
from fastapi import FastAPI, Request

app = FastAPI()

def get_env(key):
    return os.getenv(key, 'undefined')

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        # doesn't even have to be reachable
        s.connect(('10.254.254.254', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

@app.get("/myapp/info")
def read_root(request: Request):
    domain = request.base_url
    path = request.url.path
    client_host = request.client.host
    headers = request.headers

    print(f'REQUEST domain={domain} path={path}')
    return {"domain": domain,
            "path": path,
            "my_ip": get_ip() ,
            "host_hostname": get_env('HOST_HOSTNAME'),
            "client_host": client_host,
            "headers": headers
            }
