import pytest

from pyrefine.Classes.DataStructureObject import DataStructureObject
from pyrefine.DataStructures.LinkedList.LinkedListImplementer import LinkedListImplementer
from pyrefine.DataStructures.Stack.StackImplementer import StackImplementer

ENCODING='utf-8'

@pytest.mark.parametrize("obj, url", [
    (StackImplementer(), "/data-structures/stack/example/"), 
    (LinkedListImplementer(), "/data-structures/linkedlist/example/")
    ])
def test_data_structure(client, obj: DataStructureObject, url):
    title, code, examples = obj.get_template_values()
    length = len(examples)

    for i in range(length):
        example = examples[i]
        data = client.get(url + f'{i + 1}').data
        assert bytes(f'<h1>{title}</h1>', encoding=ENCODING) in data
        assert bytes(f'<span>{code}</span>', encoding=ENCODING) in data
        assert bytes(f'<h3>{example.title}</h3>', encoding='utf-8') in data
        assert bytes(f'<span>{example.description}</span>', encoding=ENCODING)in data
        assert bytes(f'<span>{example.input}</span>', encoding=ENCODING) in data
        assert bytes(f'<span class="pre-wrap">{example.output}</span>', encoding=ENCODING)  in data
        for value in example.state:
            assert bytes(f'<span class="box-value">{value}</span>', encoding='utf8') in data
        
        if i == 0:
            assert b'<input type="submit" value="Next">' in data
            assert b'<input type="submit" value="Previous" class="disabled">' in data
        elif i == length - 1:
            assert b'<input type="submit" value="Next" class="disabled">' in data
            assert b'<input type="submit" value="Previous">' in data
        else:
            assert b'<input type="submit" value="Next">' in data
            assert b'<input type="submit" value="Previous">' in data