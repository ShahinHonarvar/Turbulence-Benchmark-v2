def return_vowels(s):
    vowels = []
    for i in range(82, 90):
        if i < len(s) and 'T' < s[i] <= 'b' and (s[i] in 'aeiou'):
            vowels.append(s[i])
    return vowels