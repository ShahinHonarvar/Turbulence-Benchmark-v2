def return_vowels(text):
    vowels_list = [char for char in text[85:99] if 'f' < char <= 'n' and char in ('a', 'e', 'i', 'o', 'u')]
    return vowels_list