def return_vowels(text):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    start_index, end_index = (59, 61)
    result = []
    for ch in text[start_index:end_index]:
        if ch in vowels and ord('c') + 1 <= ord(ch) <= ord('h'):
            result.append(ch)
    return result