from pyrefine.StackImplementer import StackImplementer

def test_stack(client):
    stack = StackImplementer()
    stack.generate_examples
    response = client.get('/data-structures/stack/example/1')
    assert b'<input type="submit" value="Previous" class="disabled">' in response.data