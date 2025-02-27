def return_vowels(s):
    vowels = []
    for i in range(323, 526):
        if 43 < ord(s[i]) <= 58:
            vowels.append(s[i])
    return vowels