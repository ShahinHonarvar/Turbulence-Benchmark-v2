import re
import ast

def create__code(text_specification):
    code = re.sub('#.*', '', text_specification)
    tree = ast.parse(code)
    return tree