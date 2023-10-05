class Override:
    name: str
    override_type: str
    anchor_count: str
    def __init__(self, name, override_type, anchor_count=None) -> None:
        self.name = name
        self.override_type = override_type
        self.anchor_count = anchor_count