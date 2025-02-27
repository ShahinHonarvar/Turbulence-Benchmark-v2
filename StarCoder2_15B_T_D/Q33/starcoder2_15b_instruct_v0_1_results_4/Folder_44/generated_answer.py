def return_vowels(string):
    vowels = []
    for i in range(46, 49):
        if string[i].lower() in 'aeiou' and string[i] > '[' and (string[i] <= 'p'):
            vowels.append(string[i])
    return vowels