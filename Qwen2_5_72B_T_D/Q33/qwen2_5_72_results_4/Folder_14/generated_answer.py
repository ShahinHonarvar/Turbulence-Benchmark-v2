def return_vowels(input_string):
    vowels = 'aeiouAEIOU'
    result = []
    for char in input_string[47:61]:
        if char in vowels and ord(char) > ord('9') and (ord(char) <= ord('O')):
            result.append(char)
    return result