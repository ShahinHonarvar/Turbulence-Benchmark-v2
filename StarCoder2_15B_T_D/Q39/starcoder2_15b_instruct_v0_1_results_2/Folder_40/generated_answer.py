def return_n_greatest_chars(string):
    text_specification = "<Write a function called'return_n_greatest_chars' that takes one argument, a string of distinct characters and creates the sorted list of exactly 7 characters of the given string that have the greatest ASCII values. The function should sort the list in descending order and returns it.>"
    function_name = 'return_n_greatest_chars'
    argument_name = 'string'
    n = 7

    def return_n_greatest_chars(string):
        ascii_values = [ord(char) for char in string]
        sorted_ascii_values = sorted(ascii_values, reverse=True)
        return [chr(value) for value in sorted_ascii_values[:n]]
    return return_n_greatest_chars(string)