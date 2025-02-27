def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [char for char in s[71:81] if '>' < char <= 'U' and char in vowels]