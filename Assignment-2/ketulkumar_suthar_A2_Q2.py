# Write a function that accepts two strings. One is a search string (a sentence) and the other is the
# word we are searching for. The function returns the number of times the word is found in the sentence.

def count_word(search_string,word):
    """This function take two string as argument and return number of time word occured in string.
    search_string : String Type
    word : String Type
    """
    try:
        word_list = [word for word in search_string.split(' ')] # this logic split string by " " and convert into list
        return word_list.count(word) # this return number of count words match with search word.
    except:
        print("Invalid arguments.") # this code execute when user pass invalid arguments like True, 123
        return 0
