
from flask import Flask, request, jsonify
import jwt
import time
import requests

app = Flask(__name__)

PRIVATE_KEY = """-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCTQf8TVYsXemPV
AL9szZkLmVoPeXb4JX/lbX27LG6jY+3fd/cgdSLHm+a9HCugwu4RSOowMdhrOwM6
Q5yCf651MDJzU8JiL1DP5KwOzgP6SzTYhGyBwlp98bbNopfXVdRyQNpPSoyxqEx1
Hxjb0tF4NbmtWrHg1xdIl6+rx75BzmzHCt5J4JdeRsKI2TsdxMv7J15uzYiNTvBL
riDeflK/x+NrJgPwmTt2C8PHq1ohun3phJBdq83px44a0COXRXJXvyOtLnnRWGkS
jwHJNurL5UeleSGKwiq6g212mCaLM6Ef4/n8IbajYUD4KydwmoKfO+jF2z60JxUC
wL9O6vSJAgMBAAECggEAB3FoA6GowJyKjDsX8ddoe2oaX7rbdQpsLvv8RWgnBXIp
FUj6gDT7d4xdOsTAPcVshAoj8CCs2Cqo7Jp7QCtU9Y5klmiu5AiRNJjRy4PFNrLz
blgvJdXdfg0oGLe1pggsD0RQ5H4Xo2kmyCq0tnOu670HcAgsAnnMrvofwnZ7mtbR
CwgRyHlezU8ICO64Hbgp6R4OaB1l9cx1mGI80k3+g71Biv+LmoVcSkX65aqu+k6i
MhdB3ktyfgmRhfFt2mkrzcAFrUlS+8Sq6WJcEnTUTqwKDNkGzWjfjHAPtheloCl6
gib+enBx4qnaslfL1lRtuyWE7mcL6/SDp8pm0dzoaQKBgQC6iRZcsOFp52LYviom
naGPrOS+SrgWt3GHUOnVWmqqv696wZbKG41To8uaK5dPpa+dVwu/xyYCr7xIcFQv
e6AGx9fsvbSsusqPCymOOp/7US7sGhdpSeTgopjumi45ImRRO76SXLcRf00aeNMV
Kld5STOD5mr0ESGsErw+i2cv9QKBgQDKGHbR2koBPqQg0e3Kn2pnNvZEn+f/F/K1
sfDBaGx36Yvi8W0FMoXpUWYiS4sLruLYK2stcIN96ADfdVExcca2arRx/pWkCy6M
PVGhtYxAAhXcu1R0P865jNYyflUo+IJw4YSvROySRodGNPWtGetkkBd1TS6nOMMN
zB1+2Y+5xQKBgHgTRPTX29K7YxLYnvOKpvSAvCKOoJ/m6ErN2ChB8sYFbGVd9r4V
LE1589dDVjysEDb9UI/cF2jFTTNoM5j5QJL8088Ocx55g2i/K7nlnRQ/NzA+v3FE
YvQDVuTJFRYsQF1WUx+OVT4LL0vqGR7XycVGTMYMbi68VGubB9hPDlZ9AoGBAI6z
X5MmlAL0/GfAVCwzDKr9AD/MucBCZLsvflTTK2QwoPoKh3SYDD6Hn5qvxOrm/n6t
iex3+iE5ZQRkjoRfVnUQO4ISxg8jZibYVX/d9b5suos2K5g6Rfp3G/hjhDZ9431Z
gJtSC8ntyy8jziYAm1pS9H17lmm1huWDL4CWlwoRAoGATSEYdybQN/GxKZjHgyoC
DsBdJnd4LyehKnCLbuV+s0nPurBz5mlK4FFmS3mlMCZxNVJ/V0D07uPsh2qwIqIq
xbtbYv2rjuVgEByu59Cm/19J5jf8xrZKFSi4dZAVk58ZEzfKKfkvi3+FWB1y1PVi
iCS3JnJe19SyQnqXEphfqRA=\n-----END PRIVATE KEY-----"""
SERVICE_ACCOUNT_ID = "aje6caa6fnmr0o3vf72m"

@app.route('/get-token', methods=['POST'])
def get_token():
    now = int(time.time())
    payload = {
        "aud": "https://iam.api.cloud.yandex.net/iam/v1/tokens",
        "iss": SERVICE_ACCOUNT_ID,
        "iat": now,
        "exp": now + 3600,
    }

    encoded_jwt = jwt.encode(
    payload,
    PRIVATE_KEY,
    algorithm="PS256",
    headers={"kid": "ajemlma37b8jud9l5dm9"}
)


    response = requests.post(
        "https://iam.api.cloud.yandex.net/iam/v1/tokens",
        json={"jwt": encoded_jwt},
    )

    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": response.text}), response.status_code

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001)




