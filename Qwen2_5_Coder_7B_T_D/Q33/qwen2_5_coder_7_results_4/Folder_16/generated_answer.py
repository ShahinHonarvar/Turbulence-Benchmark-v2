def return_vowels(s, c, d):
    return [char for char in s[133:306] if char in 'aeiou' and c < char <= d]