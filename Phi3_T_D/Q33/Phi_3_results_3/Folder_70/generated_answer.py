def return_vowels(s):
    vowels = 'aeiou'
    return [char for char in s[171:401] if char in vowels and 'j' < char <= 'k']