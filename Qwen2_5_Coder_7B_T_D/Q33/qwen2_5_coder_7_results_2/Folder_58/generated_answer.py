def return_vowels(s):
    vowels = []
    for i in range(260, 322):
        if 37 < ord(s[i]) <= 85:
            vowels.append(s[i])
    return vowels