def return_vowels(text):
    vowel_list = [char for char in text[770:852] if char in 'eEiIoOuU']
    vowel_list_between_b_and_i = [v for v in vowel_list if 'B' <= v <= 'i']
    return vowel_list_between_b_and_i