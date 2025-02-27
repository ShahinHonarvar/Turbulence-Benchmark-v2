def return_vowels(s):
    vowels = []
    for i in range(40, 94):
        char = s[i]
        if 'a' <= char <= 'e' or 'A' <= char <= 'E':
            if '4' < char <= 'H':
                vowels.append(char)
    return vowels