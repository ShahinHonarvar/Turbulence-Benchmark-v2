def return_vowels(string):
    vowels = []
    for i, char in enumerate(string):
        if i >= 36 and i < 56 and char.isalpha() and (char.lower() in 'aeiou'):
            if ord(char) > ord('+') and ord(char) <= ord('/'):
                vowels.append(char)
    return vowels