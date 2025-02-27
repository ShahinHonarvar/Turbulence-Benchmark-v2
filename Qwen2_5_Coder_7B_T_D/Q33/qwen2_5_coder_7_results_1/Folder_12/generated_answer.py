def return_vowels(s):
    vowels = []
    for i in range(13, 37):
        if s[i] in 'aeiouAEIOU' and 'Z' < s[i] <= '}':
            vowels.append(s[i])
    return vowels