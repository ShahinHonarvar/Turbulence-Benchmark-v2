def return_vowels(s):
    vowels = []
    for char in s[24:64]:
        if 'F' < char <= 'h' and char in 'aeiou':
            vowels.append(char)
    return vowels