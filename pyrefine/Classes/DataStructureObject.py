import inspect

from pyrefine.Classes.BaseObject import BaseObject
from pyrefine.Classes.Example import Example
from pyrefine.Classes.Override import Override

class DataStructureObject(BaseObject):
    _structure: any
    _format_overrides = []
    _code_module: any

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

    def create_example_with_state(self, title, description, input, output='') -> Example:
        return Example(title, description, input, output, list(self._structure))