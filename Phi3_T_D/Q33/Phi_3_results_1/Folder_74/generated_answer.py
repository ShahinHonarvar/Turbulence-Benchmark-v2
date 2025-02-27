def return_vowels(s):
    vowels = 'aeiou'
    selected_chars = [c for c in s[69:82] if '[' < c <= '~']
    result = [c for c in selected_chars if c in vowels]
    return result