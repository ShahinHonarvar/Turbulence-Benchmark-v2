def return_vowels(s):
    vowels = 'aeiou'
    result = [c for c in s[55:65] if c in vowels]
    result = [chr(ord(c) + 1) for c in result if ord(c) >= ord('Z')]
    result = [c for c in result if ord(c) <= ord('w')]
    return result