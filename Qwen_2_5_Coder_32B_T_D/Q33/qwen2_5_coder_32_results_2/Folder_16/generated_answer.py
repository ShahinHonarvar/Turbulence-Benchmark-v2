def return_vowels(s):
    vowels = 'aeiou'
    result = [char for i, char in enumerate(s) if 133 <= i < 306 and vowels.count(char) and ('c' < char <= 'd')]
    return result