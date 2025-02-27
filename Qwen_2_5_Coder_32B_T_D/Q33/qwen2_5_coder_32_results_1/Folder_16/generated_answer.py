def return_vowels(s):
    vowels = 'aeiou'
    result = [char for index, char in enumerate(s) if 133 <= index < 306 and char in vowels and ('c' < char <= 'd')]
    return result