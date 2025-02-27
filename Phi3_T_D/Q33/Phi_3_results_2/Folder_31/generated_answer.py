def return_vowels(s):
    lower_bound = ord('P')
    upper_bound = ord('G')
    vowels = []
    for char in s[65:70]:
        if lower_bound < ord(char) <= upper_bound and char in 'aeiou':
            vowels.append(char)
    return vowels