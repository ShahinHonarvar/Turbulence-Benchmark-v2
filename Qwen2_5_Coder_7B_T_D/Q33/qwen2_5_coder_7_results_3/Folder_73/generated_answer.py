def return_vowels(s):
    vowels = []
    for i in range(47, 89):
        char = s[i]
        if char > '@' and char <= 'n' and (char.lower() in 'aeiou'):
            vowels.append(char)
    return vowels