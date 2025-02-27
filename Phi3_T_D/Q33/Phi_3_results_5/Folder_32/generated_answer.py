def return_vowels(s):
    return [chr(i) for i in range(ord('a') + 45, ord('a') + 76) if 'aeiou'[i % 5 - 1] > chr(ord('b')) and 'dlrst'[i % 5 - 3] >= chr('z')]