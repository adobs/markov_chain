from random import choice
from sys import argv
#first variable in argv is source 


##what this is doing


def open_and_read_file(file_path_list):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    text = ""
    for file_path in file_path_list:
        log_file = open(file_path)
        text = text + log_file.read() + " "
        log_file.close()


    return text


def make_chains(text_string, n_gram_number=None):
    """Takes input text as string; returns dictionary of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """
    words = text_string.split()

    new_dictionary = {}

    if n_gram_number == None:
        n_gram_number = int(raw_input("What do you want n in n-gram to be? "))
    


    #loop through words in words list, but ignore the last two elements
    for i in range(len(words)- n_gram_number):


        if tuple(words[i:i+n_gram_number]) not in new_dictionary:
            value = []
            key = tuple(words[i:i+n_gram_number])
            value.append(words[i+n_gram_number])
          
        else:
            key = tuple(words[i:i+n_gram_number])
            value = new_dictionary[key]
            value.append(words[i+n_gram_number])


        new_dictionary[key] = value

    return new_dictionary


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""
   
    text = ""

    # pick a random tuple from the dictionary. 
    upper_keys = []

    for key in chains.keys():
        if key[0][0].isupper():
            upper_keys.append(key)
    
    next_tuple = choice(upper_keys)
    


    # add the tuple to the text string
    # for loop to add the tuple
    for i in range(n_gram_number):
        text = text + str(next_tuple[i]) +" "
       
    text = text.strip()
        
    # while the next tuple is in the dictionary,
    # find the next value, add it to the text,
    # and create the next tuple from the last tuple and new value
    while next_tuple in chains and next_tuple[-1][-1] not in [".", "?", "!"]:
    # while next_tuple in chains and next_tuple[-1][-1] != "." and next_tuple[-1][-1] != "?" and next_tuple[-1][-1] != "!":
        next_value = choice(chains[next_tuple])
        text = text + " " + str(next_value)
        
        #for loop, going in reverse order 
        # say its tuple is three, next_tupe[-2], next tuple[-1]
    
        tuple_list = []
        for i in range(n_gram_number*-1 + 1, 0, 1):
            tuple_list.append(next_tuple[i])

        tuple_list.append(next_value)


        next_tuple = tuple(tuple_list)
  




    return text


input_path = "green-eggs.txt"
input_path2 = "gettysburg.txt"
# Open the file and turn it into one long string
input_text = open_and_read_file(argv[1:-1])

# Get a Markov chain\

if argv[-1].isdigit():
    n_gram_number = int(argv[-1]) 
else:
    n_gram_number = int(raw_input("What do you want n in n-gram to be? ")) 
chains = make_chains(input_text, n_gram_number)

# Produce random text
random_text = make_text(chains)

print random_text

