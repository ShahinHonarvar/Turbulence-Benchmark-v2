def return_vowels(s, c, d):
    vowels = 'aeiouAEIOU'
    result = [char for char in s[133:306] if char in vowels and c < char <= d]
    return result