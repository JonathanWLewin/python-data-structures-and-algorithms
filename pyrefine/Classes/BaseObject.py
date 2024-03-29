from pyrefine.Classes import Example
from pyrefine.Helpers.CodeFormatter import format_code
class BaseObject():
    _title = ''
    _code = ''
    _format_overrides = []

    def __init__(self) -> None:
        pass

    def generate_examples(self) -> Example:
        pass
    
    def get_template_values(self):
        return self._title, self.format_code_with_override(self._code), self.generate_examples_and_convert_code()
    
    def format_code_with_override(self, code) -> str:
        return format_code(code, self._format_overrides)
    
    def generate_examples_and_convert_code(self) -> Example:
        examples = self.generate_examples()
        for example in examples: 
            example.input = self.format_code_with_override(example.input)
        return examples