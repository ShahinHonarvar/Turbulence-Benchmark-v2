def return_vowels(text):
    vowels = 'aeiouAEIOU'
    return [char for char in text[529:828] if char in vowels and 'U' < char <= 'l']