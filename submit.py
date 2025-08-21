import base64
import hashlib
import hmac
import json
import struct
import sys
import time
import requests  # pip install requests

def generate_totp(secret: str, time_step: int = 30, digits: int = 10) -> str:
    counter = int(time.time() // time_step)
    msg = struct.pack(">Q", counter)
    key = secret.encode("utf-8")

    hmac_hash = hmac.new(key, msg, hashlib.sha512).digest()
    offset = hmac_hash[-1] & 0x0F
    code = struct.unpack(">I", hmac_hash[offset:offset+4])[0] & 0x7fffffff
    return str(code % (10 ** digits)).zfill(digits)

def main():
    if len(sys.argv) != 3:
        print("Usage: python submit.py YOUR_EMAIL GIST_URL")
        sys.exit(1)

    email = sys.argv[1]
    gist_url = sys.argv[2]

    secret = email + "HENNGECHALLENGE004"
    totp = generate_totp(secret)

    payload = {
        "github_url": gist_url,
        "contact_email": email,
        "solution_language": "python"
    }

    auth_str = f"{email}:{totp}"
    auth_bytes = auth_str.encode("utf-8")
    auth_header = "Basic " + base64.b64encode(auth_bytes).decode("utf-8")

    headers = {
        "Content-Type": "application/json",
        "Authorization": auth_header
    }

    url = "https://api.challenge.hennge.com/challenges/backend-recursion/004"
    response = requests.post(url, headers=headers, data=json.dumps(payload))

    print("Status:", response.status_code)
    print("Response:", response.text)

if __name__ == "__main__":
    main()
