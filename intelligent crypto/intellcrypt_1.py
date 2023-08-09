import random
import time

print("Pratham Raj Sinha 21BIT0092")
print("")

message = int(input("Enter number to be encrypted: "))
print("Original :",message)
print("")
start_time = time.time()
print("*** Encryption ***")
print("")
R = random.randint(0,message)
print("Random number: ",R)
print("")

K = random.randint(2**10142,2**10143)
print("Key: ",K)
print("")

S = message - R
print("Data split: ",S)
print("")
keygen_time = time.time() - start_time
start_time = time.time()

XOR_SK = S^K
print("XOR S AND Key: ",XOR_SK)

XOR_RK = R^K
print("XOR R and Key: ",XOR_RK)
print("")

encr_SK = int(XOR_SK)
print("Encrypted SK: ",encr_SK)
encr_RK = int(XOR_RK)
print("Encrypted RK: ",encr_RK)
print("")
encrypt_time = time.time() - start_time


print("*** Decryption ***")
start_time = time.time()
print("")
decr_SK = encr_SK^K
print("Decrypted SK: ",int(decr_SK))
decr_RK = encr_RK^K
print("Decrypted RK: ",int(decr_RK))
print("")

og_msg = decr_RK + decr_SK
decrypt_time = time.time() - start_time


print("Original msg :", og_msg)

print("")
print("Key Generation Time:", keygen_time)
print("Encryption Time:", encrypt_time)
print("Decryption Time:", decrypt_time)