
print("Welcome to the world of cryptography")

def main():
    print()
    print("Choose one option")
    choice = int(input("1. Encryption\n2. Decryption\nChoose(1,2): "))
    if choice == 1:
        encryption()
    elif choice == 2:
        decryption()
    else:
        print("Wrong Choice")


def encryption():
    print("Encryption starting...")
    msg=input("Enter your message: ")
    key=int(input("Enter your key 1-94: "))
    encrypted_text=""

    for i in range(len(msg)):
        temp=(ord(msg[i])+key)

        if temp>126:
            temp=temp-127+32
        encrypted_text+=chr(temp)
    print("encrypted", encrypted_text)

    main()


def decryption():

    print("Decryption starting...")
    print("Message can only be lower or upper case alphabet")
    encrypt_msg=input("Enter your message: ")
    decrypt_key=int(input("Enter your key 1-94: "))
    decrypted_text=""

    for i in range(len(encrypt_msg)):
        temp=(ord(encrypt_msg[i])-decrypt_key)

        if temp<32:
            temp=temp+127-32
        decrypted_text+=chr(temp)
    
    print("decrypted", decrypted_text)

        
if __name__ == "__main__":
    main()
