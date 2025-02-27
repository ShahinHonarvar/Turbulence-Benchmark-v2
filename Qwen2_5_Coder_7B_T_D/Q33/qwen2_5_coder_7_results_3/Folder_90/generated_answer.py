def return_vowels(s):
    vowels = []
    for char in s[142:145]:
        if char in 'aeiou' and 4 < ord(char) <= ord('o'):
            vowels.append(char)
    return vowels