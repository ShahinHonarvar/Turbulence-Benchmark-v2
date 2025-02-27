def return_n_greatest_chars(str):
    if len(set(str)) >= 26:
        return sorted(set(str), key=lambda x: -ord(x))[-26:]
    else:
        return sorted(set(str), key=lambda x: -ord(x))