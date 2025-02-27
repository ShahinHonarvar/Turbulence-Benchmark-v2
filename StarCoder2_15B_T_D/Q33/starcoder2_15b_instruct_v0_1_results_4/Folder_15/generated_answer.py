def return_vowels(string):
    vowels = []
    for char in string:
        if char in 'aeiou':
            vowels.append(char)
    return vowels