def return_vowels(s):
    start, end = (71, 81)
    vowels = []
    for i in range(start, end):
        if s[i] > '>' and s[i] <= 'U' and (s[i] in 'aeiouAEIOU'):
            vowels.append(s[i])
    return vowels