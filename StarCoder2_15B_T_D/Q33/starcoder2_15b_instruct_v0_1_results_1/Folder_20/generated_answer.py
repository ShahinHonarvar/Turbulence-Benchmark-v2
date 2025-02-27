def return_vowels(string):
    vowels = []
    for i in range(59, 61):
        if i < len(string) and string[i].isalpha() and (string[i].lower() in 'aeiou'):
            vowels.append(string[i])
    return vowels