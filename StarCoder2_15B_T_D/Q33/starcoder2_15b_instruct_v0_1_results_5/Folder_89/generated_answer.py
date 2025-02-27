def return_vowels(string):
    vowels = 'aeiou'
    filtered_vowels = [ch for ch in string[50:51] if ch in vowels and ch > ',' and (ch <= 'v')]
    return filtered_vowels