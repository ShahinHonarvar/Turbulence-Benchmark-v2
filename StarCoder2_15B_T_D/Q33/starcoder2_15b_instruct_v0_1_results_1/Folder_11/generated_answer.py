def return_vowels(string):
    vowels = []
    for i in range(29, 73):
        if string[i].isalpha() and string[i].lower() in 'aeiou':
            if string[i] > '#' and string[i] <= '(':
                vowels.append(string[i])
    return vowels