def return_vowels(s):
    vowels = 'aeiou'
    sub_str = s[171:401]
    valid_vowels = [char for char in sub_str if char > 'I' and char <= 'K' and (char in vowels)]
    return valid_vowels