"""
author: Alexey Aleshchenok
date: 2023-11-13
command 'encrypt' - encrypt users message, using decoder, and save it to 'txt.msg_encrypted' file
command 'decrypt' - decrypt message from 'txt.msg_encrypted' file, using decoder, and print it
"""
import sys

DECODER = {56: 'A', 57: 'B', 58: 'C', 59: 'D', 40: 'E', 41: 'F', 42: 'G', 43: 'H', 44: 'I', 45: 'J',
           46: 'K', 47: 'L', 48: 'M', 49: 'N', 60: 'O', 61: 'P', 62: 'Q', 63: 'R', 64: 'S', 65: 'T',
           66: 'U', 67: 'V', 68: 'W', 69: 'X', 10: 'Y', 11: 'Z', 12: 'a', 13: 'b', 14: 'c', 15: 'd',
           16: 'e', 17: 'f', 18: 'g', 19: 'h', 30: 'i', 31: 'j', 32: 'k', 33: 'l', 34: 'm', 35: 'n',
           36: 'o', 37: 'p', 38: 'q', 39: 'r', 90: 's', 91: 't', 92: 'u', 93: 'v', 94: 'w', 95: 'x',
           96: 'y', 97: 'z', 98: ' ', 99: ',', 100: '.', 101: ';', 102: '`', 103: '?', 104: '!', 105: ':'}


def encryption(message):
    """encrypt message, using decoder, and return it"""
    encrypt = {}
    for i in DECODER:
        encrypt[DECODER[i]] = str(i)
    new_message = []
    for i in message:
        new_message.append(encrypt[str(i)])
    message = ','.join(new_message)
    return message


def decryption(message):
    """decrypt message, using decoder, and return it"""
    lis = message.split(',')
    new_lis = []
    for i in lis:
        new_lis.append(DECODER[int(i)])
    message = ''.join(new_lis)
    return message


def save_to_file(file_name, data):
    """open file in 'write mode' and write down the data to it"""
    with open(file_name, 'w') as file:
        file.write(data)


def read_from_file(file_name):
    """open file in 'read mode', read data from it and return the data"""
    with open(file_name, 'r') as file:
        data = file.read()
    return data


def main():
    """main function"""
    if sys.argv[1] == 'encrypt':
        message = input('Enter the message to encrypt: ')
        encrypted_message = encryption(message)
        save_to_file('txt.msg_encrypted', encrypted_message)
        print('Your message saved to "txt.msg_encrypted"')
    elif sys.argv[1] == 'decrypt':
        try:
            decrypted_message = decryption(read_from_file('txt.msg_encrypted'))
            print('Decrypted message: ' + decrypted_message)
        except FileNotFoundError as msg:
            print(msg)


if __name__ == '__main__':
    main()
