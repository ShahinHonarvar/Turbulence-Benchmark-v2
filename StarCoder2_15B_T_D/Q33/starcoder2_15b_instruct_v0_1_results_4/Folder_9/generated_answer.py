def return_vowels(string):
    vowels = []
    for i in range(13, 35):
        if i > 8 and string[i] <= 'F':
            vowels.append(string[i])
    return vowels