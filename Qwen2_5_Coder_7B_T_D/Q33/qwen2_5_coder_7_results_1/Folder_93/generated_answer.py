def return_vowels(s):
    vowels = []
    for i in range(54, 82):
        if 54 <= i < 82 and 'a' <= s[i] <= 'e' or 'A' <= s[i] <= 'E':
            vowels.append(s[i])
    return vowels