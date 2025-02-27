def return_vowels(s):
    vowels = 'aeiou'
    selected_chars = s[12:39]
    res = [char for char in selected_chars if ';' < char <= '|']
    return [char for char in res if char in vowels]