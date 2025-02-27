def return_vowels(s):
    vowels = 'aeiou'
    result = [char for char in s[19:32] if vowels > char > '0' and char <= '7']
    return result