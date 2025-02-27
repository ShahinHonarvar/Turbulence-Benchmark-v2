def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    filtered_vowels = list(filter(lambda x: x > '_' and x <= 'x', vowels))
    result = [char for index, char in enumerate(string) if index >= 90 and index < 97 and (char in filtered_vowels)]
    return result