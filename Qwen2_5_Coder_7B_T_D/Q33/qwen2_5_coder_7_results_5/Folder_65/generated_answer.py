def return_vowels(s):
    return [char for char in s[71:88] if char in 'aeiouAEIOU' and 9 < ord(char) <= ord('P')]