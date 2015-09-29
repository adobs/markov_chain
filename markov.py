from random import choice
from sys import argv
#first variable in argv is source 
source, argv1, argv2 = argv

def open_and_read_file(file_path, file_path2=None):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    log_file = open(file_path)

    if file_path2 != None:
        log_file2 = open(file_path2)
        text = log_file.read() + " " + log_file2.read()
        log_file2.close()
    else:
        text = log_file.read()
    
    log_file.close()

    return text


def make_chains(text_string):
    """Takes input text as string; returns dictionary of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """
    words = text_string.split()

    answer = set()
    new_dictionary = {}


    for i in range(len(words)-2):
        #key
        # answer.add(tuple(words[i:i+2]))
        # value.append(words[i+2])


        #########masons line of thought



        # if tuple(words[i:i+2]) not in new_dictionary:
        #     key = tuple(words[i:i+2])
        #     value.append(words[i+2])

        # else:
        #     pass

        if tuple(words[i:i+2]) not in new_dictionary:
            value = []
            key = tuple(words[i:i+2])
            value.append(words[i+2])
          
        else:
            key = tuple(words[i:i+2])
            value = new_dictionary[key]
            value.append(words[i+2])


        new_dictionary[key] = value

    return new_dictionary





        #value
    # for value in answer:
        #value is the tuple of words, we want the next word that follows
        # we want to iterate through the text, returning 
   

    #print answer
    # chains = {}

    # # your code goes here

    # return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""
   
    text = ""

    # return that tuple plus one of the values from the key/list.  
    # now, use the second word from the tuple plus the random word 
    # from the list as our next tuple
    # starting_tuple = ('iterate', 'over')

    ######################
    # pick a random tuple from the dictionary.  
    next_tuple = choice(chains.keys())
    # add the tuple to the text string
    text = str(next_tuple[0]) +" " +str(next_tuple[1])
    
    while next_tuple in chains:
        next_value = choice(chains[next_tuple])
        text = text + " " + str(next_value)
        next_tuple = tuple([next_tuple[1], next_value])

    # find a random value from the key/tuple

    # add that random value to the string
    # tuple(1 of last tuple, random value)
    # find the random value
    # add that to the string


    return text


input_path = "green-eggs.txt"
input_path2 = "gettysburg.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(argv1, argv2)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text

