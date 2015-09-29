from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    log_file = open(file_path)
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
    answer = []
    text = ""

    # pick a random tuple from the dictionary.  
    # return that tuple plus one of the values from the key/list.  
    # now, use the second word from the tuple plus the random word 
    # from the list as our next tuple
    # starting_tuple = ('iterate', 'over')



    def looping_through(word1,word2,chains):
        #for a random number in lenth of the value at key, return index[random]
        value = chains[tuple([word1,word2])]
        print value
        next_word = choice(value)

        answer.extend([word1, word2, next_word])

        return looping_through(answer[-2],answer[-1], chains)

    looping_through("Would","you",chains)

    # return text


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text

