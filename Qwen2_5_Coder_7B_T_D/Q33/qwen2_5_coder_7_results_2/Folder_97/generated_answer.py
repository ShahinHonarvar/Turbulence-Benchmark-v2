def return_vowels(s):
    vowels = []
    for i in range(328, 455):
        if s[i] in 'aeiou' and s[i] > '<' and (s[i] <= 'z'):
            vowels.append(s[i])
    return vowels