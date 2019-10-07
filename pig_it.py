def pig_it(string):
    new_str = []
    for word in string.split():
        if word.isalpha():
            word = word[1:] + word[:1] + "ay"
            new_str.append(word)
        else:
            new_str.append(word)
    return ' '.join(new_str)


print(pig_it('This is my string o W !'))
