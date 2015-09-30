from random import choice
from sys import argv
#first variable in argv is source 
source, argv1, argv2 = argv

def open_and_read_file(file_path, file_path2=None):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    log_file = open(file_path)

    # if there's a second filepath provided, create the text from both
    if file_path2 != None:
        log_file2 = open(file_path2)
        text = log_file.read() + " " + log_file2.read()
        log_file2.close()

    # if no second file is provided, create the text from the single file provided
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

    new_dictionary = {}

    #loop through words in words list, but ignore the last two elements
    for i in range(len(words)-2):


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


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""
   
    text = ""

    # pick a random tuple from the dictionary.  
    next_tuple = choice(chains.keys())

    # add the tuple to the text string
    text = str(next_tuple[0]) +" " +str(next_tuple[1])
    
    # while the next tuple is in the dictionary,
    # find the next value, add it to the text,
    # and create the next tuple from the last tuple and new value
    while next_tuple in chains:
        next_value = choice(chains[next_tuple])
        text = text + " " + str(next_value)
        next_tuple = tuple([next_tuple[1], next_value])


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

