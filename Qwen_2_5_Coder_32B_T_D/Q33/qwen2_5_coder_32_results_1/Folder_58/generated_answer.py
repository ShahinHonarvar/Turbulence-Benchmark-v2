def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [char for char in s[260:322] if vowels.find(char) != -1 and '%' < char <= 'U']