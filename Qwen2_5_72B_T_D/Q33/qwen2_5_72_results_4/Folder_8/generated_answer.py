def return_vowels(s):
    vowels = 'aeiou'
    result = [char for char in s if char in vowels and ord(char) > 80 and (ord(char) <= 122) and (64 <= ord(char) < 82)]
    return result