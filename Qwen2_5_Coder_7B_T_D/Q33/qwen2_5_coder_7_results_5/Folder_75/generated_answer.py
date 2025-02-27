def return_vowels(s):
    vowels = []
    for i in range(20, 41):
        if s[i] in 'aeiouAEIOU':
            if 'K' < s[i] <= 'Z':
                vowels.append(s[i])
    return vowels