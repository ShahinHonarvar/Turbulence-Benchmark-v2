def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    filtered_vowels = filter(lambda x: ord(x) > ord('4') and ord(x) <= ord('o'), string[142:145])
    return [vowel for vowel in filtered_vowels if vowel in vowels]