def return_vowels(s):
    vowels = 'AEIOUaeiou'
    result = [char for char in s[10:82] if char > '$' and char <= '@' and (char in vowels)]
    return result