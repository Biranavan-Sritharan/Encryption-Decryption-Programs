#one thing to note is that variable and list name are quite bad, but its 4am in the morning, so i dont really care :)
#next time I will probably use dictionaries instead of chr/ord,, its just not often I get to use chr/ord


#small probelm, letter z kinda messes up, with how unicode works!!!
#ok this problem i relaised when coding the decrypt function, but is fixed by doing basically the opposite here to stop getting weird unicode symbols like { or & etc.

#Encryption function
def encrypt(plaintext , shift_key):
    #plaintext = 'aaa' #used before the input options were avaliable in testing, same for key value
    #shift_key = 1 
    plaintext_list = []

    #this basically adds the plaintext to an array, basically making each letter a char, which ord and chr functions can process
    for x in plaintext:
        plaintext_list.append(x)

    ord_list = []
    chr_list = []

    #after converting one letter to unicode value, adds the shift value to it and then adds this to a list
    for x in plaintext_list:
        convert = ord(x) + shift_key #e.g. 120 + 3 = 123, 123 - 122 = 1 <-
        if convert > 122: #122 is equivalent to z, so if we go past that we want to go to 'a' not something else in unicode
            change = convert - 122 #problem was i was doing 122 - convert
            new = change + 96
            ord_list.append(new)

        else:
            ord_list.append(convert)
    #print(ord_list) #debugging
    
    #converts the shifted unicode value back to a letter which basically forms the new cipher text in an array
    for x in ord_list:
        convert_chr = chr(x)
        chr_list.append(convert_chr)
    #print(chr_list) #debugging

    #this basically converts an array to a string which can be presented in a cleaner and nicer way
    ciphertext = ''.join(chr_list)
    print("cipher text: " + ciphertext) #ciphertext output


#Decryption, (assuming shift key value is unknown, since this is a bit more of a challenge than if you know the shift value)
def decryption(ciphertext):
    #ciphertext = 'ihuhuh' #used in debugging, it is cipher for banana
    ciphertext_len = len(ciphertext)
    ciphertext_list = []

    for x in ciphertext:
        ciphertext_list.append(x)

    ord_list = []
    for x in ciphertext_list:
        convert = ord(x)
        ord_list.append(convert)
    
    every_ord_value = [] #new list is initizalized but I probably could have reused the old list again, oh well
    #so this here is VERY important, due to the nature of chr and ord, and how they retrieve the unicode values of a letter, what if the shift key value went below 96, which is a.
    #It would give the symbol ` , so to avoid this and make it so if it goes below 'a', it loops back to 'z'! If this block was to be removed, it would still give a result but it wouldn't make any sense!
    for x in range(1,27):
        shift_key = x
        for y in ord_list:
            change_by_shift_key = y - shift_key 

            if change_by_shift_key < 97:
                new_shift = 122 - (96 - change_by_shift_key) #96!!! #made a small logic error here which I eventually worked out :), overall decrypting caesar cipher isn't too hard
                every_ord_value.append(new_shift)
            
            else:
                every_ord_value.append(change_by_shift_key)

    
    print("after if statement applied: " + str(every_ord_value))

    chr_list = []
    for x in every_ord_value:
        convert_chr = chr(x)
        chr_list.append(convert_chr)
        
    
    print("")
    print(chr_list) #the last 2 blocks of code is very much uneccessary, but i was trying to present the results in a neater way

    count = 0
    final_array = []
    for x in chr_list:
        final_array.append(x)
        count += 1
        if count == ciphertext_len:
            final_array.append('#')
            count = 0
    
    print(final_array)

    actual_final_array = []
    for x in final_array:
        if x == '#':
            print("\n")
        else:
            temp_var = "".join(x).replace('\n' , '')
            actual_final_array.append(temp_var)
            print(temp_var) #dammit presenting it nicely is harder than ACTUALLY CRACKING the cipher!!!


#can choose between encrypting or decrypting
def main():
    print("Welcome to Caesar Cipher Code Cracker (and encrypter)")
    choice = input("Type e to encrypt OR d to decrypt something: ")
    choice = choice.lower() #so capitalization doesn't affect this!

    if choice == "e":
        plaintext = input("Enter Plaintext: ")
        plaintext = plaintext.lower() #forces lowercase on plain and cipher text, since Capital letters can affect unicode values obtained from chr and ord
        shift_key = int(input("Enter how much you want to shift by: "))
        encrypt(plaintext , shift_key)

    elif choice == "d":
        ciphertext = input("Enter Ciphertext: ")
        ciphertext = ciphertext.lower()
        decryption(ciphertext)

    else:
        print("Error!")
        main()

#run as main file
if __name__ == "__main__":
    main()

# CODE MISTAKES/WORKING OUT/ UNUSED CODE # 

'''   
#this was used in debugging when looking at what lowest and highest ord/chr values would be
a = ord("a") #97
print(a)

z = ord("z") #122
print(z)
        
'''

#plaintext_variations = "".join(chr_list)
    #print(plaintext_variations[ciphertext_len])
   
    #97 = a  ,  122 = z    

'''
#this was used in debugging when looking at what lowest and highest ord/chr values would be
a = ord("b") #letter to no
print(a)

b = chr(98) #no to letter
print(b)
'''

    
    















    





