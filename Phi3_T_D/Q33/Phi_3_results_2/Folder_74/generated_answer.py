def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    filter_vowels = [char for char in text[69:82] if char in vowels and '[' < char <= '~']
    return filter_vowels