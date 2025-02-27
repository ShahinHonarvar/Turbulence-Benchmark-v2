def return_vowels(s):
    vowels = []
    for char in s[85:99]:
        if '/' < char <= 'n' and char in 'aeiou':
            vowels.append(char)
    return vowels