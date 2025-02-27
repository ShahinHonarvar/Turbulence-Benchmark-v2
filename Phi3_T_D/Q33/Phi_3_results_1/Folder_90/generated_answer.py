def return_vowels(s):
    lower_bound = 'g'
    upper_bound = 'o'
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in s[142:145] if lower_bound <= char <= upper_bound and char in vowels]
    return result