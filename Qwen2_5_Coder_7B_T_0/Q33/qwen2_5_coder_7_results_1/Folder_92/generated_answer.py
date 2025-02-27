def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for char in s[3:8] if char in vowels and ';' < char <= 'D']
    return result