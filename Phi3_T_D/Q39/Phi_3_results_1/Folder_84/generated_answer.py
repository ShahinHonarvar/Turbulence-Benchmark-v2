def return_n_greatest_chars(input_string):
    if len(input_string) < 10:
        return sorted(input_string)[-10:]
    else:
        return ''.join(sorted(input_string, reverse=True))[:10]