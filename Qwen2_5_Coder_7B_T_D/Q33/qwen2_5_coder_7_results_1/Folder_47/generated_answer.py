def return_vowels(s):
    vowels = []
    for char in s[23:38]:
        if char in 'aeiou' and 'N' < char <= 'k':
            vowels.append(char)
    return vowels