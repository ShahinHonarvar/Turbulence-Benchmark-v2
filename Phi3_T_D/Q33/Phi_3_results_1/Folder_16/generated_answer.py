def return_vowels(s):
    vowels = 'aeiou'
    start_index, end_index = (133, 306)
    c, d = ('A', 'D')
    return [char for char in s[start_index:end_index] if c < char <= d and char.lower() in vowels]