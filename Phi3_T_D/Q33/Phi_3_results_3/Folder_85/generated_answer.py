def return_vowels(s):
    result = []
    for char in s[55:65]:
        if 'A' < char <= 'W' and char in 'AEIOU':
            result.append(char)
    return result