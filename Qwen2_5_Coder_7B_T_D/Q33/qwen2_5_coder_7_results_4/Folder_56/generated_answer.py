def return_vowels(s):
    vowels = [char for char in s[15:86] if char in 'aeiouAEIOU' and '@' < char <= '~']
    return vowels