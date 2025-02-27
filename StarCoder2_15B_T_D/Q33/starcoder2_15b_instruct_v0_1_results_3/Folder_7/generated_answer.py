def return_vowels(string):
    vowels = []
    for i in range(202, 872):
        if string[i] in 'aeiou' and string[i] > '3' and (string[i] <= '>'):
            vowels.append(string[i])
    return vowels