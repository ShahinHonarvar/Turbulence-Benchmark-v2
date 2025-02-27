def return_vowels(s):
    vowels = 'aeiou'
    result = [char for char in s[1:4] if char.lower() in vowels and 'c' < char.lower() <= 'i']
    return result