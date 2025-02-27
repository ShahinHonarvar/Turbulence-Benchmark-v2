def return_vowels(s):
    vowels = 'aeiou~'
    result = [char for char in s[170:645] if vowels.find(char) != -1]
    return result