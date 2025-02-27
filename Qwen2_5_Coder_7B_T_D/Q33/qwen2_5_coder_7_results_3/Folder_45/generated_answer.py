def return_vowels(s):
    vowels = []
    for i in range(43, 70):
        char = s[i]
        if char > '*' and char <= 'b' and (char in 'aeiou'):
            vowels.append(char)
    return vowels