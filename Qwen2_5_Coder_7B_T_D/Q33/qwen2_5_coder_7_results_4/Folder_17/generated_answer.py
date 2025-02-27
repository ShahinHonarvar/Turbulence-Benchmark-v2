def return_vowels(s):
    vowels = []
    for i in range(60, 99):
        if 106 < ord(s[i]) <= 110:
            vowels.append(s[i])
    return vowels