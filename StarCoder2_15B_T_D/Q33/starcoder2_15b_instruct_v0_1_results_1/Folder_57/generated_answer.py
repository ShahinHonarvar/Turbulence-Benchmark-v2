def return_vowels(string):
    vowels = []
    for char in string[21:23]:
        if char.isalpha() and char.lower() in 'aeiou' and (char > '-') and (char <= 'n'):
            vowels.append(char)
    return vowels