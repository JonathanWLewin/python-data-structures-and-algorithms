import pytest

from pyrefine.Classes.AlgorithmBaseObject import AlgorithmBaseObject
from pyrefine.Algorithms.AddTwoNumbers.AddTwoNumbersImplementer import AddTwoNumbersImplementer
from pyrefine.Algorithms.TwoSum.TwoSumImplementer import TwoSumImplementer

ENCODING='utf-8'

@pytest.mark.parametrize("obj, url", [
        (AddTwoNumbersImplementer(), "/algorithms/add-two-numbers/method/{}/example/{}/step/{}"),
        (TwoSumImplementer(), "/algorithms/two-sum/method/{}/example/{}/step/{}")
    ])
def test_algorithm(
    client, 
    obj: AlgorithmBaseObject, 
    url
    ):
    '''
        Test values shared by all algorithm objects
    '''
    
    # Test each method
    for method in obj.methods:
        # Test each example
        for i in range(len(obj.examples)):
            # Generate the example and steps
            title, code, example_values, examples, methods, anchor = obj.get_template_values(
                example=i,
                custom_example_input=None,
                target=None,
                method=method
            )

            # Pull steps from the example_values
            steps = example_values["steps"]
            # Get the length of the steps for enumerating through values
            length = len(steps)
            

            for j in range(length):
                formatted_url = url.format(method, i + 1, j + 1)
                data = client.get(formatted_url).data
                # Pull current step from steps
                step = steps[j]
                if "values_to_display" in step:
                    for key in step["values_to_display"]:
                        assert bytes(f'''<span>{key}</span>
        {step["values_to_display"][key]}''', encoding=ENCODING) in data

                assert bytes(f'<h1>{title}</h1>', encoding=ENCODING) in data
                assert bytes(f'<span>{code}</span>', encoding=ENCODING) in data
                assert bytes(f'Example {i + 1}', encoding=ENCODING) in data
                assert bytes(f'<input type="submit" value="Example {i + 1}">', encoding=ENCODING)in data

                
                assert b'<input type="submit" value="Custom">' in data
                if length == 1:
                    assert b'<input type="submit" value="Next" class="disabled">' in data
                    assert b'<input type="submit" value="Previous" class="disabled">' in data
                elif j == 0:
                    assert b'<input type="submit" value="Next">' in data
                    assert b'<input type="submit" value="Previous" class="disabled">' in data
                elif j == length - 1:
                    assert b'<input type="submit" value="Next" class="disabled">' in data
                    assert b'<input type="submit" value="Previous">' in data
                else:
                    assert b'<input type="submit" value="Next">' in data
                    assert b'<input type="submit" value="Previous">' in data


def test_add_two_numbers(client):

    '''
        Test add two numbers algorithm
    '''

    obj = AddTwoNumbersImplementer()
    for method in obj.methods:

        '''
        =================================
        Check Preset examples
        =================================
        '''
        for i in range(len(obj.examples)):
             
            example_values, steps, length = get_template_values_and_extras_for_add_two_numbers(i, None, obj)

            for j in range(length):
                url = f"/algorithms/add-two-numbers/method/{method}/example/{i + 1}/step/{j +  1}"
                # Retrieve data from client
                data = client.get(url).data

                # Check a few simple values
                assert bytes(f'<h2>Example {i + 1}</h2>', encoding=ENCODING) in data
                assert bytes(f'<span>Input: L1: {example_values["input"]["L1"]}, L2: {example_values["input"]["L2"]}</span>', encoding=ENCODING) in data
                assert bytes(f'<span>Expected output: {example_values["output"]}</span>', encoding=ENCODING) in data

                step = steps[j]
                check_special_content_for_add_two_numbers(step, example_values, data)

        '''
        =================================
        Check Custom Example Default
        =================================
        '''

        custom_example_input = {
            "L1": [5, 8, 3, 6, 7],
            "L2": [6, 7, 8, 1, 4]
        }

        example_values, steps, length = get_template_values_and_extras_for_add_two_numbers(None, custom_example_input, obj)
        

        for j in range(length):
            url = f"/algorithms/add-two-numbers/method/{method}/example/custom/step/{j +  1}"
            # Retrieve data from client
            data = client.get(url).data

            # Check a few simple values
            assert bytes(f'<input name="l1Input" id="l1Input" value="{custom_example_input["L1"]}" required>', encoding=ENCODING) in data
            assert bytes(f'<input name="l2Input" id="l2Input" value="{custom_example_input["L2"]}" required>', encoding=ENCODING) in data

            step = steps[j]
            check_special_content_for_add_two_numbers(step, example_values, data)


        '''
        =================================
        Check Custom Example Post
        =================================
        '''

        custom_example_input_for_url = {
            "l1Input": '[6, 9, 8, 7, 4, 1]',
            "l2Input": '[8, 9, 6, 1, 7, 5, 3]'
        }

        custom_example_input = {
            "L1": [6, 9, 8, 7, 4, 1],
            "L2": [8, 9, 6, 1, 7, 5, 3]
        }

        example_values, steps, length = get_template_values_and_extras_for_add_two_numbers(None, custom_example_input, obj)

        url = f"/algorithms/add-two-numbers/method/{method}/example/custom/step/{1}"
        # Retrieve data from client
        data = client.post(url, data=custom_example_input_for_url).data
        
        # Check a few simple values
        assert bytes(f'<input name="l1Input" id="l1Input" value="{custom_example_input["L1"]}" required>', encoding=ENCODING) in data
        assert bytes(f'<input name="l2Input" id="l2Input" value="{custom_example_input["L2"]}" required>', encoding=ENCODING) in data

        step = steps[0]
        check_special_content_for_add_two_numbers(step, example_values, data)

        '''
        =================================
        Check Custom Example Get
        =================================
        '''

        custom_example_input = {
            "L1": [6, 9, 8, 7, 4, 1],
            "L2": [8, 9, 6, 1, 7, 5, 3]
        }

        custom_example_input_for_url = "{'L1':[6, 9, 8, 7, 4, 1],'L2':[8, 9, 6, 1, 7, 5, 3]}"

        example_values, steps, length = get_template_values_and_extras_for_add_two_numbers(None, custom_example_input, obj)

        for j in range(len(steps)):
            url = f"/algorithms/add-two-numbers/method/{method}/example/custom/step/{j + 1}/{custom_example_input_for_url}"
            # Retrieve data from client
            data = client.get(url).data
            
            # Check a few simple values
            assert bytes(f'<input name="l1Input" id="l1Input" value="{custom_example_input["L1"]}" required>', encoding=ENCODING) in data
            assert bytes(f'<input name="l2Input" id="l2Input" value="{custom_example_input["L2"]}" required>', encoding=ENCODING) in data

            step = steps[j]
            check_special_content_for_add_two_numbers(step, example_values, data)

def get_template_values_and_extras_for_add_two_numbers(example, custom_example_input, obj):
    title, code, example_values, examples, methods, anchor = obj.get_template_values(
        example=example,
        custom_example_input=custom_example_input
    )

    # Pull steps from the example_values
    steps = example_values["steps"]
    # Get the length of the steps for enumerating through values
    length = len(steps)

    return example_values, steps, length

def check_special_content_for_add_two_numbers(step, example_values, data):
    # Get lengths for link count checks and for enumeration
    input_l1_length = len(example_values["input"]["L1"])
    input_l2_length = len(example_values["input"]["L2"])
    values_arr_length = len(step["values_arr"])
    # Check number of links based on values (should be doubled because footer data is duplicated)
    assert data.count(b'<span class="linked-list-link"></span>') == (input_l1_length + input_l2_length + values_arr_length - 3) * 2

    for ind1 in range(input_l1_length):
        if step["L1"]:
            check_boxes(ind1, step["L1"].id, data, example_values, "L1")
    for ind2 in range(input_l2_length):
        if step["L2"]:
            check_boxes(ind2, step["L2"].id, data, example_values, "L2")

def check_boxes(ind, id_value, data, example_values, L_lookup):
    if ind == id_value:
        assert bytes(f'''<div class="box-blue">
                <span class="box-value">{example_values["input"][L_lookup][ind]}</span>
            </div>''', encoding=ENCODING) in data
    else:
        assert bytes(f'''<div class="box">
                <span class="box-value">{example_values["input"][L_lookup][ind]}</span>
            </div>''', encoding=ENCODING) in data