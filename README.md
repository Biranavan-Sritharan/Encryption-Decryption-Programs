# Encryption-Decryption-Programs
Some python projects I made for encrypting and decrypting data using different cryptographic techniques from basic algorithms like Caesar shift to RSA (at some point)

NOTE: Just want to mention that comments in these programs aren't exactly industry standard but more to show you my thought process :)

Caesar Cipher Decryption and Encryption program:

This was done in fairly easily in about a day, Caesar shift is not too complicated to work with but the standard way I would say to do this task is using dictionaries but instead I used chr/ord methods instead since it is not often, I get to use these methods and I thought it would be nice to use these. Also, for decryption of Caesar cipher, I thought it would be too easy to be given the shift key value so it will display every possible outcome (26 outcomes) just for an added layer of challenge. But the hardest part of this was trying to display the final outcome in a nice manner. Also using NumPy library probably would have made it more efficient but not necessary!

Frequency Analysis:

This was completed in just one or two hours and was much simpler than I initially thought. But this is used alongside with any Vigenère or substitution ciphers that would require and frequency analysis attacks for decryption. No libraries are needed :) Also using NumPy library probably would have made it more efficient but not necessary!

Vigenère Cipher Encryption and Decryption:

Since last time I used ord/chr methods, and I wanted to use a dictionary this time, that is what I did. The way the dictionary was initialized to bring up the alphabet was better than just typing out the whole alphabet with corresponding values because that would have taken too long! And what if I wanted to add other languages too, then I would be here all day trying to type all those values, so initializing the dictionary is more semi-automated where the alphabet from a to z was stored in a variable which took about 10 seconds to type out, then the rest of the values (numbers, colons etc.) was added with a for loop which saved a lot of time. Encrypting plaintext with Vigenère cipher isn't too hard since it follows similar mechanics to Caesar cipher. There is a way to fully automate the dictionary initialization by importing the string library, but I didn’t look too much into it because I wanted to focus on the cryptographic area of this project.

