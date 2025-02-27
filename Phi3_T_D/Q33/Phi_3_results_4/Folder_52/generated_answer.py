def return_vowels(text):
    vowels = 'aeiou'
    selected_range = text[24:68]
    return [char for char in selected_range if f < char <= '|' and char in vowels]