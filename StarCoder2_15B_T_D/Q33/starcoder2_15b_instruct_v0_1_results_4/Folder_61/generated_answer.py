def return_vowels(string):
    vowels = []
    for i in range(1, 4):
        if string[i].lower() in 'aeiou' and 'c' < string[i] <= 'i':
            vowels.append(string[i])
    return vowels