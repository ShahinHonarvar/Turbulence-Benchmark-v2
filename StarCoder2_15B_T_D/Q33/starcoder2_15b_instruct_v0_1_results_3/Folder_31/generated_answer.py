def return_vowels(string):
    vowels = []
    for char in string:
        if char.isalpha() and char in 'aeiou' and (65 < ord(char) <= 70) and (char > '%') and (char <= 'G'):
            vowels.append(char)
    return vowels