def return_vowels(text):
    vowels = 'aeiou'
    target_index_range = text[13:35]
    result = [char for char in target_index_range if char in vowels and 'h' <= char <= 'F']
    return result