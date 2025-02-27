def return_vowels(s):
    vowels = []
    for i in range(77, 84):
        if 'a' <= s[i] <= 'g' and s[i] in 'aeiou':
            vowels.append(s[i])
    return vowels