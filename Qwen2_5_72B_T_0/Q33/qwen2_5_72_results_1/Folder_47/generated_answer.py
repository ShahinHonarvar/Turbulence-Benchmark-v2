def return_vowels(s):
    vowels = 'aeiou'
    return [char for char in s[23:38] if char.lower() in vowels and 'N' < char <= 'k']