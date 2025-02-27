def return_vowels(s):
    vowels_greater_n_but_less_than_equal_l = [char for char in s[604:949] if 'N' < char <= 'U' and char in 'AEIOUaeiou']
    return vowels_greater_n_but_less_than_equal_l