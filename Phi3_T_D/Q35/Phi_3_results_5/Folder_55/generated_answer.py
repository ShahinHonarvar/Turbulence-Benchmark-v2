from collections import OrderedDict

def remove_repeat_chars(input_string):
    filtered_string = OrderedDict.fromkeys(input_string[10:100]).keys()
    altered_string = ''.join(filtered_string) + input_string[100:]
    return altered_string