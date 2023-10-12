import inspect
from pyrefine.Helpers.CodeFormatter import format_code

from pyrefine.Classes.Override import Override

class AlgorithmBaseObject():
    _title = ''
    _code_module: any
    _format_overrides = []
    _examples = []

    def __init__(self) -> None:
        self.get_format_overrides_from_code()
        self.get_code()
        super().__init__()

    def get_format_overrides_from_code(self):
        for cls in inspect.getmembers(self._code_module, inspect.isclass):
            self._format_overrides.append(Override(cls[0], 'class'))
            self._format_overrides += [Override(x[0], 'func') for x in inspect.getmembers(cls[1], inspect.isfunction)]
    
    def get_code(self):
        self._code = inspect.getsource(self._code_module)
    
    def format_code_with_override(self, code) -> str:
        return format_code(code, self._format_overrides)
    
    def get_template_values(self, example=1):
        return self._title, self.format_code_with_override(self._code), self.generate_example(example_number=example), self._examples
    
    def generate_steps(self):
        pass

    def generate_example(self, example_number=None, inputted_example=None):
        pass