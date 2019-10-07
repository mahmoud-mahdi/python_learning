import socket, ssl
import random, string
import hashlib, crypt

authdata = ""
host = 'srv.exatest.dynu.net'
port = 3335
cert_file = 'certchain.pem'
key_file = 'private.key'


# def random_string():
#    return ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(8))


def hash_function(authdata, difficulty):
    while True:
        suffix_string = crypt.mksalt()
        string_to_hash = authdata + suffix_string
        cksum_in_hex = hashlib.sha1(string_to_hash.encode('utf-8')).hexdigest()
        if cksum_in_hex.startswith("0" * difficulty):
            break
    return suffix_string


def message_encrypt(authdata, args_1, message):
    return hashlib.sha1(authdata + args_1 + " " + message + "\n").hexdigest().encode('utf-8')


# CREATE SOCKET
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sock.settimeout(10)

# WRAP SOCKET
wrappedSocket = ssl.wrap_socket(sock, keyfile=key_file, certfile=cert_file, ssl_version=ssl.PROTOCOL_TLSv1_2)

# CONNECT TO THE SERVER
wrappedSocket.connect((host, port))
#args = wrappedSocket.read().decode('utf-8').strip().split(' ')

while True:

    args = wrappedSocket.read().decode('utf-8').strip().split(' ')

    # CHECK RESPONSE FROM SERVER
    if args[0] == "HELO":
        wrappedSocket.sendall("EHLO\n".encode('utf-8'))

    elif args[0] == "ERROR":
        print("ERROR: " + " ".join(args[1:]))
        break

    elif args[0] == "POW":
        print("POW recieved: " + args[1])
        authdata, difficulty = args[1], int(args[2])
        suffix = hash_function(authdata, difficulty)
        wrappedSocket.sendall((suffix + "\n").encode('utf-8'))
        print("Suffix string is: " + suffix + "\n")

    elif args[0] == "END":
        # if you get this command, then your data was submitted
        wrappedSocket.sendall("OK\n".encode('utf-8'))
        print("All data has been sent")

        break

    elif args[0] == "NAME":
        # as the response to the NAME request you should send your full name
        # including first and last name separated by single space

        print("Sending the Name")
        message_to_send = message_encrypt(authdata, args[1], "Mahmoud Mahdi")
        wrappedSocket.sendall(message_to_send)

    elif args[0] == "MAILNUM":
        # here you specify, how many email addresses you want to send
        # each email is asked separately up to the number specified in MAILNUM

        message_to_send = message_encrypt(authdata, args[1], "1")
        wrappedSocket.sendall(message_to_send)

    elif args[0] == "MAIL1":

        message_to_send = message_encrypt(authdata, args[1], "mahmoud.abdelgalel87@gmail.com")
        wrappedSocket.sendall(message_to_send)

    elif args[0] == "SKYPE":

        # here please specify your Skype account for the interview, or N/A
        # in case you have no Skype account

        message_to_send = message_encrypt(authdata, args[1], "mahmoud.abdelgalel")
        wrappedSocket.sendall(message_to_send)

    elif args[0] == "BIRTHDATE":

        # here please specify your birthdate in the format %d.%m.%Y

        message_to_send = message_encrypt(authdata, args[1], "01.01.1987")
        wrappedSocket.sendall(message_to_send)

    elif args[0] == "COUNTRY":

        # country where you currently live and where the specified address is
        # please use only the names from this web site:

        #   https://www.countries-ofthe-world.com/all-countries.html

        message_to_send = message_encrypt(authdata, args[1], "Czechia")
        wrappedSocket.sendall(message_to_send)

    elif args[0] == "ADDRNUM":

        # specifies how many lines your address has, this address should
        # be in the specified country

        message_to_send = message_encrypt(authdata, args[1], "2")
        wrappedSocket.sendall(message_to_send)

    elif args[0] == "ADDRLINE1":

        message_to_send = message_encrypt(authdata, args[1], "Purkynova 83")
        wrappedSocket.sendall(message_to_send)

    elif args[0] == "ADDRLINE2":

        message_to_send = message_encrypt(authdata, args[1], "61200 Brno")
        wrappedSocket.sendall(message_to_send)


# CLOSE SOCKET CONNECTION
wrappedSocket.close()

