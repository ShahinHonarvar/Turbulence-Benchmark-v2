def return_vowels(s):
    vowels = []
    for i in range(40, 94):
        if s[i] in 'AEIOUaeiou' and 4 < ord(s[i]) <= ord('H'):
            vowels.append(s[i])
    return vowels