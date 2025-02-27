def return_vowels(s):
    result = []
    for char in s[22:82]:
        if char > 'N' and char <= 'o' and (char in 'aeiouAEIOU'):
            result.append(char)
    return result