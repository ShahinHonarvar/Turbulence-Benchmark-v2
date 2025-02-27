def return_vowels(s):
    vowels = 'aeiou'
    result = [char for index, char in enumerate(s) if 495 <= index < 837 and char in vowels and (char > 'B') and (char <= 't')]
    return result