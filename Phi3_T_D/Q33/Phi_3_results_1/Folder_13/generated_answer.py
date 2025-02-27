def return_vowels(s):
    vowels = 'AEIOUaeiou'
    range_of_indices = slice(149, 313)
    within_range = s[range_of_indices]
    selected_vowels = [c for c in within_range if c in vowels and 'M' < c <= 'j']
    return selected_vowels