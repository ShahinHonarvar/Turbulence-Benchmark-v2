def return_vowels(s):
    vowels = []
    for i in range(34, 69):
        if 97 <= ord(s[i]) <= 111:
            vowels.append(s[i])
    return vowels