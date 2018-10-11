
user_value=input('Please enter a value: ')
if user_value>50:
    print('Big number!')
else:
    print('Small Number! ')

    
#Laboratory troubleshooting
print('Laboratory troubleshooting')

does_it_move=input('Does it move? Yes/No ')

does_it_move.lower()
if does_it_move=='yes':
    should_it=input('Should it? Yes/No ')
    should_it.lower()
    if should_it=='yes':
        print('No problem!')
    else:
        print('Use Tape!!!')

else:
    should_it=input('Should it? Yes/No ')
    should_it.lower()
    if should_it=='yes':
        print('Use WD-40!!!')
    else:
        print('No problem!')

#Printing numbers


numbers=[2,3,4,5]
for number in numbers:
    print(f'My number is {number*12}' )

 

#Palindromes
def palindrome(word):
    #result=True
    word_length=len(word)
    if word_length%2==0:
        for i in range (0,word_length//2):
            if word[i]!=word[word_length-1-i]:
                return False
    else:
        for i in range (0,(word_length-1)//2):
            if word[i]!=word[(word_length-1)-i]:
                return False
    return True

word=input("Please enter a word to see if it's Polidrome: ")
palindrome(word)
if palindrome(word)==False:
    print('not palindrome')
else:
    print('palindrome')
