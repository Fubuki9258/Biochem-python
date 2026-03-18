def find(word, letter):
    index = 0
    for i in word:
        if i == letter:
            return index
        else:
            index += 1

    
print(find("test word", "d"))