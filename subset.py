'''Module for all possible words from a subset of characters'''

from itertools import permutations
import urllib.request

def sub_set():
  """
  Function to get all possible wors from a subset of characters from each input word
  Args:
    None
  Returns:
    list : A list of all possible subset of characters
  """
  
  #get all possible english words
  response =  urllib.request.urlopen("https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt").read()
  possible_words = response.decode().split('\r\n')
 
  #define lists
  possible_list =[]
  input_list = ["cat", "dog", "sun", 'photo']

  #get all permutations from each input word
  for item in input_list:
    possible_items = [perm for length in range(1, len(item) + 1) for perm in permutations(item, length)]
    
    #convert from tuple to string
    for item in possible_items:
      possible_string = ''.join(item)
      
      #check if the subset is in possible english words
      if possible_string in possible_words and possible_string not in possible_list:
        possible_list.append(possible_string)

    #print the output
  for item in possible_list:
    print(item)

#call the above function 
sub_set()
