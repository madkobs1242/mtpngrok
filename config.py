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
AUTHTOKEN = "17SUf7F65grAa2uj2Kj8ng6rLWNah4Y5x6_454aHosTH3z383L1Q2kUu"  # set to your ngrok's token
AD_TAG = "a6354ff32533943bbd871586f95aca3f"
