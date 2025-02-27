def return_vowels(string):
    vowels = []
    for i in range(8, 9):
        if string[i] in 'aeiou':
            if string[i] > 'Y' and string[i] <= 's':
                vowels.append(string[i])
    return vowels