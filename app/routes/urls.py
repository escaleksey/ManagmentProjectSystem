import os

url = os.environ["URL"]
port = os.environ["PORT"]
USER_URL = f"http://{url}:{port}" + "/user"

AUTH_URL = f"http://{url}:{port}" + "/user"