def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [char for char in s[11:53] if vowels.__contains__(char) and '+' < char <= 'W']