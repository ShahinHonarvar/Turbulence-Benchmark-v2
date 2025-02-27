def return_vowels(s):
    vowels = []
    for char in s[170:645]:
        if 'E' < char <= '~' and char in 'AEIOUaeiou':
            vowels.append(char)
    return vowels