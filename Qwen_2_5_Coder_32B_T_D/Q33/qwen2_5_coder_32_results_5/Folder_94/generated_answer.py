def return_vowels(s):
    vowels = []
    for i in range(40, 94):
        if '4' < s[i] <= 'H' and s[i] in 'AEIOUaeiou':
            vowels.append(s[i])
    return vowels