from pyrefine.DataStructures.Stack.StackImplementer import StackImplementer

def test_nav_buttons(client):
    stack = StackImplementer()
    examples = stack.generate_examples()
    response_1 = client.get('/data-structures/stack/example/1')
    assert b'<input type="submit" value="Previous" class="disabled">' in response_1.data
    response_2 = client.get(f'/data-structures/stack/example/{len(examples)}')
    assert b'<input type="submit" value="Next" class="disabled">' in response_2.data

def test_stack_examples(client):
    stack = StackImplementer()
    examples = stack.generate_examples()

    for i in range(len(examples)):
        response = client.get(f'/data-structures/stack/example/{i+1}')
        example = examples[i]
        assert bytes(f'<h3>{example.title}</h3>', encoding='utf-8') in response.data

        output = example.output
        state = example.state
        if output != '':
            assert b"output" in response.data
            assert bytes(f'<span class="pre-wrap">{output}</span>', encoding='utf8') in response.data
        else:
            assert b"output" not in response.data

        for value in state:
            assert bytes(f'<span class="box-value">{value}</span>', encoding='utf8') in response.data