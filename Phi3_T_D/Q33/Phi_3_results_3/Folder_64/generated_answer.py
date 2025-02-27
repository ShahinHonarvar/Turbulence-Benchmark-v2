def return_vowels(s):
    vowels_result = []
    vowels = 'aeiou'
    for char in s[1:7]:
        if char in vowels and ord(char) > ord('F') and (ord(char) <= ord('j')):
            vowels_result.append(char)
    return vowels_result