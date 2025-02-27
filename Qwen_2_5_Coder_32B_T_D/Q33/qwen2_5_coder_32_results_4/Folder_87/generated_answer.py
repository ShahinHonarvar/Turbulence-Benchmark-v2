def return_vowels(s):
    vowels = []
    for i in range(34, 58):
        if 'b' < s[i] <= 'o' and s[i] in 'aeiou':
            vowels.append(s[i])
    return vowels