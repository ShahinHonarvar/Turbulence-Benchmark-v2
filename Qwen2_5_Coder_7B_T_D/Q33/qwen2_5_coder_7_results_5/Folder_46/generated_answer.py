def return_vowels(s):
    vowels = []
    for i in range(10, 83):
        if 37 < ord(s[i]) <= 101:
            vowels.append(s[i])
    return vowels