def return_vowels(string):
    vowels = []
    for i in range(56, 90):
        char = string[i]
        if char.isalpha() and char.lower() in 'aeiou' and (char > 'K') and (char <= 'z'):
            vowels.append(char)
    return vowels