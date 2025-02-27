def return_vowels(s):
    vowels = 'aeiou'
    filtered_vowels = [char for char in s[1:9] if vowels.count(char) > 0]
    return filtered_vowels