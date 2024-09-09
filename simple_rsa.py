from string import ascii_lowercase as letters

#default pub_k = 13
#default priv_k = 37
#fdefault n = 60

pub_k = 5
priv_k = 11
n = 14  #this is the value that goes along with public and priv key

plaintext = "abcdefghijklmnoqrstuvwxyz"
ciphertext = ""
print("original plaintext: " + plaintext)

#setting up numbered alphabet
numbers = list(map(str, range(0, len(letters)+1)))
let_to_num = dict(zip(letters, numbers))
num_to_let = dict(zip(numbers, letters))
#print(let_to_num)
#print(num_to_let)


###Encryption###

#converting plaintext to int
num_plain = []
for x in plaintext:
    for y in let_to_num:
        if x == y:
            temp = int(let_to_num.get(y))
            num_plain.append(temp)
            #print(num_plain)

#encrypt plaintext
cipher_num = []
for x in num_plain:
    temp = (x**pub_k)%n
    cipher_num.append(str(temp))
    #print(cipher_num)

#numbered cipher back to plaintext
encrypted = []
for x in cipher_num:
    for y in num_to_let:
        if x == y:
            temp = num_to_let.get(y)
            encrypted.append(temp)
            #print(encrypted)

ciphertext = ''.join(encrypted)
print("ciphertext: " + ciphertext)
#one small limitation, the letter a which is 0 on the numbered alphabet when done with the encrpytion calc. will result in 1 
#BUT 14^5mod14 will also result in 0, so both letters a and o will have same cipher value, fix: use larger n value, i guess

###Decryption###

#convert cipher to num
num_cipher = []
for x in ciphertext:
    for y in let_to_num:
        if x == y:
            temp = let_to_num.get(y)
            num_cipher.append(int(temp))
            #print(num_cipher)

#decrypt cipher
plain_num = []
for x in num_cipher:
    temp = (x**priv_k)%14
    plain_num.append(str(temp))
    #print("plan num: " + str(plain_num))

#plain num to text
decrypted = []
for x in plain_num:
    for y in num_to_let:
        if x == y:
            temp = num_to_let.get(y)
            decrypted.append(temp)
            #print("decrypted " + str(decrypted))

plaintext = ''.join(decrypted)
print("plaintext: " + plaintext)

#ok so overall its ok BUT a larger value than 14 needs to be used, something bigger than 26 i guess hmmmmmmmm
