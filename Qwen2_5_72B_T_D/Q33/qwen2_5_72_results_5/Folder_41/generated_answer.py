def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [ch for ch in s[71:81] if ch > '>' and ch <= 'U' and (ch in vowels)]