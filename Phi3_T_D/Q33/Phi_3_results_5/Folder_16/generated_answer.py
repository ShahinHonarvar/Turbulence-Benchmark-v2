def return_vowels(s, c, d):
    vowels = {chr(i) for i in range(ord('a'), ord('z') + 1) if chr(i) in 'aeiou'}
    result = [char for char in s[133:306] if c < char <= d and char in vowels]
    return result