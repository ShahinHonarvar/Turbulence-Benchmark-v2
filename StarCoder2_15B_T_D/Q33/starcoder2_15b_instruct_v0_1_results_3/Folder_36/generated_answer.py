def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if c in 'aeiouAEIOU' and 604 <= i < 949:
            vowels.append(c)
    return vowels