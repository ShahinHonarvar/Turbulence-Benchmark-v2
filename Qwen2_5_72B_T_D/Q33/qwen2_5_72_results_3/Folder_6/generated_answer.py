def return_vowels(s):
    vowels = 'AEIOUaeiou'
    filtered_vowels = [char for char in s[20:34] if char in vowels and 'U' < char <= 'i']
    return filtered_vowels