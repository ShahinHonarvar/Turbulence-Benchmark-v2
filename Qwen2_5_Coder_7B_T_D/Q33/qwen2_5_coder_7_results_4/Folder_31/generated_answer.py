def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for char in s[65:70]:
        if char in vowels and '%' < char <= 'G':
            result.append(char)
    return result