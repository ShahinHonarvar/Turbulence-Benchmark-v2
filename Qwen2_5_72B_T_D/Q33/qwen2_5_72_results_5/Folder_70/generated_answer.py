def return_vowels(s):
    vowels = 'aeiou'
    return [char for char in s[171:402] if char in vowels and 'i' < char <= 'k']