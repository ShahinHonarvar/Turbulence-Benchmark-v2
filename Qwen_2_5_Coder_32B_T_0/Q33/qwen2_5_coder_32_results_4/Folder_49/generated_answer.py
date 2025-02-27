def return_vowels(s):
    vowels = []
    for i in range(10, 97):
        if 'R' < s[i] <= 'b' and s[i] in 'aeiou':
            vowels.append(s[i])
    return vowels