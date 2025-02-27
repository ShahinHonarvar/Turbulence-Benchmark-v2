def return_vowels(s):
    vowels_in_range = []
    for char in s[8:9]:
        if char > 'Y' and char <= 's' and (char in 'aeiouAEIOU'):
            vowels_in_range.append(char)
    return vowels_in_range