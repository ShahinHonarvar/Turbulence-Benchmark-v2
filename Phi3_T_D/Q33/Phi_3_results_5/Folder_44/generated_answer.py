def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    subset_vowels = [x for x in s[45:49] if x >= '[' and x <= 'p' and (x in vowels)]
    return subset_vowels