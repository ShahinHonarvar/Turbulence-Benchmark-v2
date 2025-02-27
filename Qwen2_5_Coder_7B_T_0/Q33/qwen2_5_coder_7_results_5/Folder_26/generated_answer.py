def return_vowels(s):
    vowels = []
    for i in range(10, 82):
        if s[i] in 'aeiouAEIOU' and '$' < s[i] <= '@':
            vowels.append(s[i])
    return vowels