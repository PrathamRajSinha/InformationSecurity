import random
import math

print("21BIT0092 Pratham Raj Sinha")
print("")
print("")
#Getting p and q and checking if they are prime
m = int(input("Enter the message: "))
p = int(input("Enter first prime number: "))
q = int(input("Enter second prime number: "))

print("Message = ",m)
def is_prime(n):
    if n < 2:
        return False

    # Check divisibility up to the square root of n
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True
while not is_prime(p):
    print("First number is not prime")
    p = int(input("Enter first prime number: "))
    
while not is_prime(q):
    print("Second number is not prime")
    q = int(input("Enter second prime number: "))
print("")
print("***KEY GENERATION***")

#KEY GENERATION

phi = (p-1)*(q-1)
n = p*q
print("p = ",p)
print("q = ",q)
print("phi = ",phi)
print("n = ",n)

#randomizing e such that it is coprime with phi
e = random.randint(2,phi-1)

#since all prime numbers are coprime, we can also select e as a prime number using is_prime(e)
#public key generation
while math.gcd(e, phi) != 1 and e!= p and e!= q: #checking for coprime
    e = random.randint(2, phi - 1)
    print("Public key e = ",e)
#private key generation
# Private Key
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return g, x, y

u = 1;
while (1+(u*2320))%e != 0:
    u+=1
d = round((1+(u*2320)/e),2)
print("d= ",d)  # Calculate the modular multiplicative inverse of e modulo phi
print("Process d = ", d)

print("")
print("***ENCRYPTION***")
#ENCRYPTION
r = random.randint(2,phi-1)
while math.gcd(r,n) != 1:
    r = random.randint(2,phi-1)
print("r = ",r)

#blind factor
bf = pow(r, e, n)

print("Blind factor = ",bf)

#blind message
bm = (pow(r, e, n) * m) % n

print("Blind message = ",bm)

#storing blind message in cloud1
cloud1 = "blindmessage.txt"
with open(cloud1, "w") as bmsg:
    bmsg.write(str(bm))
    
# SIGN GENERATION
print("")
print("***SIGN GENERATION***")
#receiving blind message from cloud1
with open(cloud1, "r") as bmsg:
    bmsg.read(int(bm))
print("Blind message from cloud = ",bm)

sg = (bm**d)%n
print("Sign generated = ",sg)

#storing sign in cloud 2
cloud2 = "sign.txt"
with open(cloud2, "w") as sign:
    sign.write(str(sg))

print("")
print("***SIGN VERIFICATION***")
#SIGN VERIFICATION

with open(cloud2, "r") as sign:
    sign.read(int(sg))
k = 0

sv = pow(r, -1, n)
print("Sign Verified = ", sv)
bdm = (sg * sv) % n #Blinded Message
print("Blinded Message = ", bdm)
bdm = int(bdm)
e = int(e)
n = int(n)
fm = pow(bdm, e, n)
print("The Computed Message = ", fm)


#final authentication
if fm == m:
    print("Authenticated signer")
else:
    print("Unauthenticated signer")


