import random
import time
print("21BIT0092 Pratham Raj Sinha")

message = int(input("Enter number to be encrypted: "))
print("Original :",message)
print("")
print("*** Encryption ***")
print("")

#random number generation
R = random.randint(1,message)
print("Random number: ",R)
print("")
r1 = bin(R)[2:]
r = r1[2:]

#random key generation
start_time = time.time()
K = random.randint(2**2048,2**2049)
print("Key: ",K)
print("")
k1 = bin(K)[2:]
k = k1[2:]

#Data split
S = message - R
print("Data split: ",S)
print("")
s1 = bin(S)[2:]
s = s1[2:]

max_len = max(len(r), len(k), len(s))
r = r.zfill(max_len)
k = k.zfill(max_len)
s = s.zfill(max_len)

XOR_SK = ''
for i in range(max_len):
    if s[i] == k[i]:
        XOR_SK += '0'
    else:
        XOR_SK += '1'
keygen_time = time.time() - start_time
print("XOR S AND Key: ",XOR_SK)

XOR_RK = ''
for i in range(max_len):
    if r[i] == k[i]:
        XOR_RK += '0'
    else:
        XOR_RK += '1'
        
print("XOR R and Key: ",XOR_RK)
print("")

encr_SK = int(XOR_SK)
print("Encrypted SK: ",encr_SK)
cloud1 = "SK.txt"
with open(cloud1, "w") as f1:
    f1.write(str(encr_SK))
    
encr_RK = int(XOR_RK)
print("Encrypted RK: ",encr_RK)
print("")

cloud2 = "RK.txt"
with open(cloud2, "w") as f2:
    f2.write(str(encr_RK))
encr_RK = int(XOR_RK)
encrypt_time = time.time() - start_time


print("*** Decryption ***")
print("")
start_time = time.time()

with open(cloud1, "r") as f1:
    a1 = f1.read()
decr_SK1 = ''
for j in range(max_len):
    if a1[i] == k[i]:
        decr_SK1 += '0'
    else:
        decr_SK1 += '1'
        

decr_SK = int(decr_SK1,2)

print("Decrypted SK: ",int(decr_SK))
with open(cloud2,"r") as f2:
    b1 = f2.read()

decr_RK1 = ''
for i in range(max_len):
    if b1[i] == k[i]:
        decr_RK1 += '0'
    else:
        decr_RK1 += '1'
        
decr_RK = int(decr_RK1,2)


decrypt_time = time.time() - start_time

print("Decrypted RK: ",int(decr_RK))
print("")

og_msg = decr_RK + decr_SK

print("Original msg :", og_msg)

print("")
print("Key Generation Time:", keygen_time)
print("Encryption Time:", encrypt_time)
print("Decryption Time:", decrypt_time)

