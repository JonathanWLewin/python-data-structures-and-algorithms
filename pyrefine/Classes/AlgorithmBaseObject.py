import inspect
from pyrefine.Helpers.CodeFormatter import format_code

from pyrefine.Classes.Override import Override

class AlgorithmBaseObject():
    _title = ''
    _code_module: any
    _format_overrides = []
    _examples = []
    _methods = []
    _anchors = {}

    def __init__(self) -> None:
        self.get_format_overrides_from_code()
        self.get_code()
        super().__init__()

    def get_format_overrides_from_code(self):
        # Get format overrides passed in as well as find members in a module to automatically override
        for cls in inspect.getmembers(self._code_module, inspect.isclass):
            self._format_overrides.append(Override(cls[0], 'class'))
            self._format_overrides += [Override(x[0], 'func') for x in inspect.getmembers(cls[1], inspect.isfunction)]
    
    def get_code(self):
        # Pull code in string form from the code module
        self._code = inspect.getsource(self._code_module)
    
    def format_code_with_override(self, code) -> str:
        # format code for display and override formatting as needed
        return format_code(code, self._format_overrides)
    
    def get_template_values(self, example=None, custom_example_input=None, target=None, method=None):
        # Pull values required for template and return
        return (
            self._title, 
            self.format_code_with_override(self._code), 
            self.generate_example(
                example_number=example,
                custom_example_input=custom_example_input, 
                target=target,
                method=method
            ), 
            self._examples,
            self._methods,
            self._anchors[method]
        )
    
    def generate_steps(self):
        pass

    def generate_example(self, example_number=None, custom_example_input=None, target=None, method=None):
        pass