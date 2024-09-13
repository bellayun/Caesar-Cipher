alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] #26 letters
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your messeage:\n").lower()
shift = int(input("Type the shift number:\n"))
print(text) 

# if new index > 25, say that it's 30, 30-26 = 4
# TODO1: Create a function called encrypt() that takes 'original_text' and 'shift_amount' as two inputs
def encrypt(original_text,shift_amount):
    original_index = []
    new_index = []
    new_text = []
  
    # find the index of original_text from alphabet list
    for i in list(original_text):
        original_index.append(alphabet.index(i))
    
    # take the original_index, and add each index with the shift_amount, then store it to new_index
    for j in (original_index):
        new_index.append(int(j) + shift_amount)
    
    # according to new index, find the corresponding letter from alphabet and place it in 'new_text'.
    # if the index exceeds 25 (which is the end of the alphabet), go back to the 0th index in alphabet list.
    for j in new_index:
        if j > len(alphabet)-1:
            new_index = int(j)-26
            new_text.append(alphabet[new_index])
        else:
            new_text.append(alphabet[j])


   
   # print original text, indices of those letters in alphabet list, indices that have been shifted, and encoded text
   # print(original_text)
   # print(original_index)
   # print(new_index)
    print(new_text)


    


# TODO2: Inside the function encrypt(), take the 'original_text' and shift each letter by 'shift_amount', and print the encrypted text

# TODO4: What happens if you want to shift z forwards by 9? Can you fix the code?

# TODO3: Call the encrypt() function and pass in the user inputs. You should be able to read the message 
encrypt(text,shift)
