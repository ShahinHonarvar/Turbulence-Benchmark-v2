def return_vowels(s):
    vowels = [chr(i) for i in range(ord('a'), ord('z') + 1) if chr(i) in 'aeiou']
    return [char for char in s[22:82] if char in vowels and char > 'N' and (char <= 'o')]