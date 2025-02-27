def return_vowels(s):
    vowels = 'aeiou'
    result = [ch for ch in s[11:61] if ch.lower() in vowels and 'm' < ch.lower() <= 'w']
    return result