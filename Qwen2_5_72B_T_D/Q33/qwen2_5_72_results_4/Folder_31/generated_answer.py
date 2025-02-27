def return_vowels(s):
    vowels = 'AEIOU'
    result = []
    for char in s[65:70]:
        if 'F' > char >= '%' and char <= 'G' and (char in vowels):
            result.append(char)
    return result