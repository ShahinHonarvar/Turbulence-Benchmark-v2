def return_vowels(s):
    vowels = []
    for i in range(13, 35):
        if s[i] in 'aeiouAEIOU' and ord(s[i]) > 8 and (ord(s[i]) <= 70):
            vowels.append(s[i])
    return vowels