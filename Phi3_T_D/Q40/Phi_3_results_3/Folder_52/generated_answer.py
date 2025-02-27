def return_n_smallest_chars(s):
    result = [ord(char) for char in s]
    result.sort()
    return [chr(char) for char in result][:68]