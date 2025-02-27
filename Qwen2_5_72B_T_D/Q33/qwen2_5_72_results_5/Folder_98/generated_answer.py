def return_vowels(s):
    vowels = 'aeiou'
    result = [char for char in s[3:9] if char.lower() in vowels and 'S' < char <= 'U']
    return result