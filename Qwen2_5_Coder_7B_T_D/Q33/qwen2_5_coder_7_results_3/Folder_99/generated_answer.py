def return_vowels(s):
    vowels = []
    for i in range(323, 526):
        if 'a' <= s[i] <= 'e' or 'A' <= s[i] <= 'E':
            vowels.append(s[i])
    return vowels