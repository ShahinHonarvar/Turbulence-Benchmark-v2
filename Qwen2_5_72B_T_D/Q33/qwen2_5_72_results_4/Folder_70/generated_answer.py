def return_vowels(s):
    vowels = 'aeiou'
    filtered_vowels = [char for char in s[171:402] if char in vowels and 'I' < char <= 'k']
    return filtered_vowels