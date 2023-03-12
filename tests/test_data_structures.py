from pyrefine.StackImplementer import StackImplementer

def test_stack_nav_buttons(client):
    stack = StackImplementer()
    examples = stack.generate_examples()
    response_1 = client.get('/data-structures/stack/example/1')
    assert b'<input type="submit" value="Previous" class="disabled">' in response_1.data
    response_2 = client.get(f'/data-structures/stack/example/{len(examples)}')
    assert b'<input type="submit" value="Next" class="disabled">' in response_2.data