def return_n_greatest_chars(string):
    sorted_string = sorted(string, key=lambda c: ord(c), reverse=True)
    extracted_chars = sorted_string[:47]
    return list(extracted_chars)