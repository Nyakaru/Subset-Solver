'''Module for all possible words from a subset of characters'''

import urllib.request

#get all english words
response =  urllib.request.urlopen("https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt").read()
english_words = response.decode().split('\r\n')

#define the input list
input_list = ['cat','dog','museum','typewriter','photosynthesis']

#define an empty dictionary
trie = {}

#build a trie of all english words
for word in english_words:
    cur = trie
    for item in word:
        cur  = cur.setdefault(item, {}) # returns the value of a key (if the key is in dictionary). If not, it inserts key with a value to the dictionary
    cur['word'] = True # word denotes the trie has this word as item
        # if word doesn't exist, trie doesn't have this word but as a path to longer word
     
def generate_words(word, trie = trie, cur = '', gen_words = []):
    """
    Function to get all possible wors from a subset of characters from each input word
    Args:
    word(str): Word in input list
    trie(dict): Search tree
    cur(str): Previous pattern of trie
    gen_words(list): List of words
    Returns:
    list : List of all possible generated words
    """
    
    for i, letter in enumerate(word): #loop over a list and retrieve both the index and the value of each item in the list
        if letter in trie: #check if letter exists in trie
            if 'word' in trie[letter]: #check if trie denotes a complete word
                gen_words.append(cur + letter) #append to the generated words list
            generate_words(word[:i] + word[i+1:], trie[letter], cur+letter, gen_words) #recursively call the function
    return gen_words

#define empty lists
word_list =[]
possible_words = []

# call the above function
for item in input_list:
    del word_list[:] #clear the word list on each iteration
    word_list = generate_words(item)
    possible_words.extend(set(word_list)) #add only unique words generated from each input word

#print the output
for item in possible_words:
  print(item)
