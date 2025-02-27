def return_vowels(s):
    vowels = []
    for i in range(260, 322):
        if i < len(s) and '%' < s[i] <= 'U' and (s[i] in 'AEIOUaeiou'):
            vowels.append(s[i])
    return vowels