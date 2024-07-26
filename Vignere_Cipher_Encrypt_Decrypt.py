def encryption(key, plaintext):
    alphabet = {}
    alpha = 'abcdefghijklmnopqrstuvwxyz'

    #creates numbered alphabet in dictionary without having to type out numbered alphabet dictionary manually
    for x in range(26):
        alphabet[alpha[x]] = x

    #print(alphabet) #debug

    #key = "KEY"
    key = key.lower()
    #plaintext = "mango" #used in debug, also cipher for this is welqs if key = key

    #makes given letter key into numerical value
    key_value = []
    for x in key:
        key_value.append(alphabet.get(x))

    #print("KEY: " + str(key_value)) #debug

    plaintext_num = []
    for x in plaintext:
        plaintext_num.append(alphabet.get(x))

    #print("PLAINTEXT VALUE: " + str(plaintext_num))#debug

    #creates the cipher but still in number format
    key_count = 0
    count = 0
    cipher_value = []
    for x in plaintext_num:
        if key_count >= len(key_value):
            key_count = 0

        value = key_value[key_count] + x
        cipher_value.append(value)
        key_count += 1

        if cipher_value[count] >= 26: #recieved a small error where is the letter w was shifted by letter e, so position 22 and key 4, then it would land on 26, originally this had >26 not >=26, so 26 would appear as None, this change fixed the code :)
            cipher_value[count] = (cipher_value[count] - 26)
        count += 1

    #print("CIPHER VALUE: " + str(cipher_value)) #debug

    #this basically reverses the id and key values in the original dictionary, so that i can then obtain a letter from the numbers obtained from before
    reversed_alphabet = {value: key for key, value in alphabet.items()}
    #print(reversed_alphabet.get(22)) #debug

    #conversion from numbers to letters from dictionary which has been reversed to make comparison easier
    cipher_list = []
    for x in cipher_value:
        cipher_list.append(reversed_alphabet.get(x))
        
    #print("This is your ciphertext: " + str(ciphertext)) #debug

    #final output here :)
    ciphertext = ''.join(str(cipher_list))
    print("Ciphertext: " + ciphertext)
   
plaintext = input("Enter plaintext you want to encrypt: ")
key = input("Enter a letter-ed key to shift your plaintext by: ")

encryption(key, plaintext)




