def return_vowels(s):
    vowels = 'aeiou'
    result = [char for i, char in enumerate(s) if 1 <= i < 9 and 'a' <= char <= 'k' and (char in vowels)]
    return result