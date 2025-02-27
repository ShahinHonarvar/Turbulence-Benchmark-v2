def return_vowels(s):
    vowels = 'aeiou'
    return [char for char in s if char in vowels and 64 <= ord(char) < 82 and ('P' < char <= 'z')]