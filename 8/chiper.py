from encrypt import encrypt


x = True

while x:
    code = str(input("Type 'encode' to encrypt, type 'decode' to decrypt: \n"))
    message = str(input('Type your message: \n')).lower()
    n = int(input('Type the shift number: \n')) % 28
    encrypted = encrypt(message, n, code)
    print ( encrypted)
    repeat = input("Type 'yes' if you want to fo again. Otherwise type 'no': ")
    if repeat == 'no':
        x = False


