
# This program print words in ascending order which are input by user

if __name__ == '__main__':
    word_list = []
    while True:
        try:
            word = input('Enter some text :') # take input from user
            if word in word_list: # this logic check word exist in list or not
                break
            else:
                word_list.append(word)
        except Exception as e:
            print(e)

    for word in sorted(word_list):# sorted function sort list into sorted order
        print(word)
