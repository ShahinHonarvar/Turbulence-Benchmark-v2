def return_vowels(text):
    vowels = 'aeiouAEIOU'
    return [char for char in text[51:77] if 'A' < char <= 'Z' and char in vowels]