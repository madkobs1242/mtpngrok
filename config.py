import os

os.chdir(os.path.dirname(__file__))

PORT = 4443
USERS = {
    "tg": open("secret", "r").read() if os.path.exists("secret") else "",
}

MODES = {
    "classic": False,
    "secure": False,
    "tls": True,
}

TLS_DOMAIN = "www.ngrok.com"
AUTHTOKEN = "1roJy4fNx5PQFHJIrVArfV5fepQ_454aHosTH3z383L1Q2kUu"  # set to your ngrok's token
AD_TAG = "d4110d66c864e65ae931cac8694aa4c5"
