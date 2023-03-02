class BaseObject():
    _title = ''
    _description = ''
    _code = ''

    def __init__(self) -> None:
        pass

    def generate_examples(self):
        pass
    
    def get_template_values(self):
        return (self._title, self._description, self._code, self.generate_examples())