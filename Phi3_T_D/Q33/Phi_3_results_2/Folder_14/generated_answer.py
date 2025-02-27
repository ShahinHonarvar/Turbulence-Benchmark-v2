def return_vowels(s):
    return [char for char in s[47:61] if 9 < ord(char) <= ord('O') and char in 'aeiouAEIOU']