import bcrypt
import crypt, hashlib


POW = "fRAlGXbcAHFcogkwOsbglDOZGjiHkXoxkUAbBIvctDHeDHdSJUwFwcRXNsbIRnAj"


while True:
    salt = crypt.mksalt()
    #salt = bcrypt.gensalt()
    auth = POW + salt
    cksum_in_hex = hashlib.sha1(auth.encode()).hexdigest()

    if cksum_in_hex.startswith("0" * 2):
        print(type(salt))
        print(cksum_in_hex)

        break
