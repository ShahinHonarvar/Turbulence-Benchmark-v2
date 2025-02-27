def return_vowels(s):
    vowels = []
    for i in range(10, 82):
        if i < len(s) and '$' < s[i] <= '@' and (s[i] in 'AEIOUaeiou'):
            vowels.append(s[i])
    return vowels