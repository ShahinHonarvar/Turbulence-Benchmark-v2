def return_vowels(s):
    vowels = 'aeiou'
    target_chars = [char for char in s[60:99] if 'j' < char <= 'n']
    return [char for char in target_chars if char in vowels]