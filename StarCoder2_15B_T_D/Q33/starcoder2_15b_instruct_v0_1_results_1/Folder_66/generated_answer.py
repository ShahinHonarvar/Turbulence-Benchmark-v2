def return_vowels(string):
    vowels = []
    for i in range(63, 79):
        if i < len(string) and string[i] in 'aeiou' and (string[i] > 'd') and (string[i] <= 'y'):
            vowels.append(string[i])
    return vowels