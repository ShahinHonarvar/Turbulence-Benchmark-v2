def return_vowels(string):
    vowels = []
    for char in string[133:306]:
        if char in 'aeiou' and char > 'c' and (char <= 'd'):
            vowels.append(char)
    return vowels