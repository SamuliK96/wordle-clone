# wordle program

import random as rand
wordlist = open('sgb-words.txt')
wordlist = wordlist.read()
wordlist = wordlist.split('\n')
ans =  rand.choice(wordlist) # This will be the correct wordle
letters = '' # Used letters
guesses = [] # Used words
n = 0 # n of guesses


while True:
    word = input('Enter a five-letter word. ')
    if len(word) != 5:
        print(f'The word {word} has {len(word)} letters, when it is supposed to have 5.')
        continue
    elif word not in wordlist:
        print(f'The word {word} is not a word.')
        continue
    elif word in guesses:
        print(f'You have already guessed {word}.')
        continue
    elif word == ans:
        n += 1
        break
    else:
        None
    
    result = ''
    for i in range(0,5):
        if word[i] in letters:
            print(f'{word[i]} has already been used in a guess.')
            break
        elif word[i] == ans[i]:
            result += 'g'
        elif word[i] in ans:
            result += 'y'
        else:
            result += 'b'
            

    n += 1
    guesses += word
    letters += word
    if len(result) == 5:
        print(result)

print(f'The correct word is {ans}. You used {n} guesses.')
