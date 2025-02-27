def return_vowels(s):
    vowels = []
    for i in range(70, 76):
        if '3' < s[i] <= ':':
            if s[i] in 'aeiouAEIOU':
                vowels.append(s[i])
    return vowels