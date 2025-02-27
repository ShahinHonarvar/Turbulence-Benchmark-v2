def return_vowels(string):
    vowels = []
    for i in range(len(string)):
        if i >= 55 and i < 65:
            if string[i].isalpha() and string[i].lower() in 'aeiou':
                if string[i] > 'Z' and string[i] <= 'w':
                    vowels.append(string[i])
    return vowels