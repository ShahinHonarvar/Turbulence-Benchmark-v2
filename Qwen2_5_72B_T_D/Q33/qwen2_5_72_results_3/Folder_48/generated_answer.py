def return_vowels(s):
    vowels = 'aeiou'
    result = [c for c in s[529:828] if c > 'U' and c <= 'l' and (c in vowels)]
    return result