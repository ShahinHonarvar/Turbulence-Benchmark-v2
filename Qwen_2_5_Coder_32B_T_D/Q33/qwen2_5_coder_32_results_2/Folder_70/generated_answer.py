def return_vowels(s):
    vowels = []
    for i in range(171, 402):
        if i < len(s) and 'I' < s[i] <= 'k' and (s[i] in 'aeiou'):
            vowels.append(s[i])
    return vowels