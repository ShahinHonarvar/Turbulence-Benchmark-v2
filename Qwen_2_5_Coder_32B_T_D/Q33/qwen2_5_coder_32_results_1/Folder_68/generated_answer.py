def return_vowels(s):
    vowels = 'aeiou'
    result = [char for char in s[1:9] if char > '?' and char <= 'k' and (char in vowels)]
    return result