def return_vowels(s):
    vowels = 'aeiouAEIOU'
    filtered_vowels = [char for char in s[69:82] if char in vowels and 'Z' < char <= '~']
    return filtered_vowels