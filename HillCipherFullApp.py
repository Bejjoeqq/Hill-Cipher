from HillCipherEncrypt import *
from HillCipherDecrypt import *
import os,sys
def cls():
    if os.name=="nt":
        os.system("cls")
    else:
        os.system("clear")
    print("Hill Cipher Converter Pro")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━")
def main():
    cls()
    exit=False
    print("Application By Bejjo, Welcome :)")
    input("Enter...")
    while True:
        try:
            cls()
            print("1. Hill Cipher Encoder\n2. Hill Cipher Decoder\n3. Exit")
            n=int(input("\nChoose Program : "))
            if n==1:
                cls()
                Encrypt()
            elif n==2:
                cls()
                Decrypt()
            elif n==3:
                exit=True
                sys.exit()
        except:
            if exit==True:
                sys.exit()
if __name__ == '__main__':
    main()
