def return_vowels(s):
    vowels = []
    for i in range(34, 58):
        if s[i] in 'aeiou' and 'b' < s[i] <= 'o':
            vowels.append(s[i])
    return vowels