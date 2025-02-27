def return_vowels(s):
    vowels = []
    for char in s[12:39]:
        if ';' < char <= '|' and char in 'aeiouAEIOU':
            vowels.append(char)
    return vowels