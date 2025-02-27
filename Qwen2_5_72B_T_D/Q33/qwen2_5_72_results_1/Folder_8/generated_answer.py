def return_vowels(s):
    vowels = 'aeiou'
    result = [char for char in s if char.lower() in vowels and 64 <= ord(char) < 82 and ('P' < char <= 'z')]
    return result