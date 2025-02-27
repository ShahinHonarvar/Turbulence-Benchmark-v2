def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [letter for letter in s[51:77] if letter in vowels and 'E' <= letter <= 'Z']