def main(text):

    #text = '' #used in debug

    #makes string an array
    text_list = []
    for x in text:
        text_list.append(x)

    #print(text_list)
    text_length = len(text_list)
    #print(text_length) #debug

    #finds unique letters in array
    unique_letters = []
    for x in text_list:
        if x not in unique_letters:
            unique_letters.append(x)
    #print(unique_letters) #debug

    #finds amounts of times each unique letter from list occurs in the general text and then calculates the percentage of how often it appears in the text
    text_count = []
    count = 0
    current_count = 0
    for x in unique_letters:
        current_letter = unique_letters[count]
        count += 1
        for x in text_list:
            if current_letter == x:
                current_count += 1
        text_count.append(current_letter)
        text_count.append(str(round((current_count/text_length)*100 , 4)) + "%") #so i could have set up another for loop etc. to neatly look through array and do calculation, but so much easier to just do calculation here
                                                                                #also just more efficent in general than having another block of code to do this calculation, originally just current_count, also made the number into a string and added %, to make it more presentable
        current_count = 0 #allows each letter to have its own count instead of a cumilative count of all letter before it, small error i ran it here which I fixed :)

    print("text count: " + str(text_count))

print("NOTE: For vignere cipher decryption it is better to have a large text sample to enter in general practice, but this can give results on any text size!")
text = input("Enter the text you want letter frequency analysis done on: ")
main(text)

