import re

def create__code(text_specification):
    text = re.search('<(.+)>', text_specification).group(1)
    function_name, parameters, logic = text.split(' that takes ')
    function_name = function_name.strip()
    parameters = parameters.strip().strip('()')
    logic = logic.strip().strip('.')
    _code = f'\ndef {function_name}({parameters}):\n    sum = 0\n    for i in range(62, 100):\n        if {logic}[i] % 2!= 0:\n            sum += {logic}[i]\n    return sum\n'
    return _code