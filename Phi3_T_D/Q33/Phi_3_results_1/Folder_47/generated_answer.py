def return_vowels(s):
    vowels = []
    start, end = (23, 38)
    for i in range(start, end):
        if s[i] in 'aeiou' and s[i] > 'n' and (s[i] <= 'k'):
            vowels.append(s[i])
    return vowels