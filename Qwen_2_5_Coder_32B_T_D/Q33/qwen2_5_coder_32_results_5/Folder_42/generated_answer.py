def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [char for char in s[12:39] if vowels.count(char) > 0 and ';' < char <= '|']