def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [char for char in s[37:57] if vowels.find(char) != -1 and '*' < char <= 'P']