def return_vowels(s):
    vowels = 'aeiou'
    result = [char for i, char in enumerate(s) if 64 <= i < 82 and 'P' < char <= 'z' and (char in vowels)]
    return result