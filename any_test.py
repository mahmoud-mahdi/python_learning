import hashlib, random, string, secrets

authdata = "fRAlGXbcAHFcogkwOsbglDOZGjiHkXoxkUAbBIvctDHeDHdSJUwFwcRXNsbIRnAj"


# def random_string():
#    return ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(8))

while True:
    # suffix = random_string()
    suffix = secrets.token_hex(6)
    new_string = authdata + suffix
    cksum_in_hex = hashlib.sha1(new_string.encode('utf-8')).hexdigest()
    if cksum_in_hex.startswith("0"*9):
        print(cksum_in_hex)

        break
