def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [char for char in s[56:96] if vowels.count(char) and '&' < char <= 'T']