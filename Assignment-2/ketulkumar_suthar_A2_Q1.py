

if __name__ == '__main__':
    word_list = []
    while True:
        word = input('Enter some text :')
        if word in word_list:
            break
        else
            word_list.append(word)

    print('/n'.join(word_list))
