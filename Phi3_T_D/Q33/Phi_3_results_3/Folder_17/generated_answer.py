def return_vowels(text):
    vowels = 'aeiouAEIOU'
    required_range = text[60:99]
    return [char for char in required_range if char > 'j' and char <= 'n' and (char in vowels)]