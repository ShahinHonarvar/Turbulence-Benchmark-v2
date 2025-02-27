def return_vowels(string):
    vowels = []
    for i in range(20, 43):
        if string[i].isalpha() and string[i].lower() in 'aeiou' and (string[i] > '5') and (string[i] <= 'M'):
            vowels.append(string[i])
    return vowels