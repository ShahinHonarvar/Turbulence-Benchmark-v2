def return_vowels(text):
    vowels = 'aeiouAEIOU'
    start_index = 71
    end_index = 88
    return [char for char in text[start_index:end_index] if 'A' <= char <= 'P' and char in vowels]