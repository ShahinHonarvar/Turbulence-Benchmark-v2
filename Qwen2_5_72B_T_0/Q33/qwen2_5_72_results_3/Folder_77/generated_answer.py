def return_vowels(s):
    vowels = 'aeiou'
    return [char for char in s[837:975] if char.lower() in vowels and 'N' < char <= 'W']