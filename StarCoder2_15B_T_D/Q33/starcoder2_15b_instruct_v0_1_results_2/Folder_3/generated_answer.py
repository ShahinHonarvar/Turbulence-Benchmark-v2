def return_vowels(string):
    vowels = []
    for i in range(50, 77):
        if i < len(string) and string[i].isalpha() and (string[i].lower() in 'aeiou') and (string[i] > '#') and (string[i] <= 'r'):
            vowels.append(string[i])
    return vowels