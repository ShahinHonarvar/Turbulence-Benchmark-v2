def return_vowels(s):
    vowels_gt_n_lt_u = [ch for ch in s[604:949] if 'N' < ch <= 'U' and ch in 'AEIOUaeiou']
    return vowels_gt_n_lt_u