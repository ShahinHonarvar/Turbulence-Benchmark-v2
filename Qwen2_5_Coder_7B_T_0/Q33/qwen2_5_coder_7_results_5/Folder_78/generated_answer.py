def return_vowels(s):
    vowels = []
    for i in range(46, 90):
        char = s[i]
        if char in 'aeiouAEIOU' and '@' < char <= '[':
            vowels.append(char)
    return vowels