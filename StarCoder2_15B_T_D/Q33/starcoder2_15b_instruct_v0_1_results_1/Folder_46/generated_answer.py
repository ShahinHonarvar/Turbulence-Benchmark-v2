def return_vowels(string):
    vowels = []
    for i, char in enumerate(string):
        if char in 'aeiou' and 10 <= i < 83 and (char > '%') and (char <= 'e'):
            vowels.append(char)
    return vowels