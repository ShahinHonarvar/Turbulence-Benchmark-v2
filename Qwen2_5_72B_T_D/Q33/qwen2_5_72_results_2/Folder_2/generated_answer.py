def return_vowels(text):
    vowels = 'aeiouAEIOU'
    return [char for char in text[170:645] if char in vowels and 'E' < char <= '~']