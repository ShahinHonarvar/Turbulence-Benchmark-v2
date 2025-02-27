def return_vowels(s):
    vowels = []
    for i in range(63, 79):
        char = s[i]
        if char in 'AEIOUaeiou' and char > 'D' and (char <= 'y'):
            vowels.append(char)
    return vowels