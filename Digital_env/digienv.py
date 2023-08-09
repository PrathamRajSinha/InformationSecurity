import math
import random
def conbin(num):
    binary = bin(num)[2:]  # Convert to binary and remove the '0b' prefix
    return binary
def bindec(binary):
    decimal = int(binary, 2)
    return decimal

msg = int(conbin(int(input("Enter message: "))))
k = int(conbin(random.randint(2**2048, 2**2049)))
print("")
print("Key = ",k)
xor_mk = int(conbin(msg^k))
print("")
print("Encrypted message = ", xor_mk)
pk = int(input("Enter public key: "))
xor_pkk =  int(conbin(k^pk))
print("")
print("Encrypted symmetric key: ", xor_pkk) 
