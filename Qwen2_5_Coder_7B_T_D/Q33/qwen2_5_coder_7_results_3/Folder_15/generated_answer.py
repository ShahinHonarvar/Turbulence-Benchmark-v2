def return_vowels(s):
    vowels = []
    for i in range(5, 6):
        char = s[i]
        if 'a' <= char <= 'e' or 'A' <= char <= 'E':
            if char > '3' and char <= '^':
                vowels.append(char)
    return vowels