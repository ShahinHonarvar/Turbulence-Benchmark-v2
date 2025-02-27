def return_vowels(s):
    vowels = []
    for char in s[90:97]:
        if char > '_' and char <= 'x':
            vowels.append(char)
    return vowels