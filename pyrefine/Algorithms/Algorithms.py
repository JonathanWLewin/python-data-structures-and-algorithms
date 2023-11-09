from flask import Blueprint, render_template, abort, request
from pyrefine.Algorithms.TwoSum.TwoSumImplementer import TwoSumImplementer
from pyrefine.Algorithms.AddTwoNumbers.AddTwoNumbersImplementer import AddTwoNumbersImplementer
import json

bp = Blueprint("algorithms", __name__, url_prefix="/algorithms")

@bp.route("two-sum/method/<string:method>/example/<int:example>/step/<int:id>")
@bp.route("two-sum/method/<string:method>/example/custom/step/<int:id>", methods=["GET", "POST"])
@bp.route("two-sum/method/<string:method>/example/custom/step/<int:id>/<string:custom_example_input>/<string:target>", methods=["GET", "POST"])
def twoSum(id=1, example=None, custom_example_input=None, target=None, method=None):
    twoSum = TwoSumImplementer()
    title = None
    code = None
    example_values = None
    examples = None
    # Example does not need to be passed in, if it is passed in subtract one for the index
    example_in = example - 1 if example is not None else None
    if request.method == 'POST':
        # Post implies a custom example
        id = 1
        custom_example_input = request.form['input']
        target = request.form['target']
        # Form data is brought in as a string, so we need to format it for int and list values
        custom_example_input, target = format_custom_example_input_and_target(custom_example_input, target)
    else:
        if example is not None:
            # If example is not None and either id or example are less than 1 then the url does not exist
            if example < 1 or id < 1:
                abort(404)
        elif custom_example_input is not None and target is not None:
            # custom example data can still be brought in through url parameters. These also need to be formatted
            custom_example_input, target = format_custom_example_input_and_target(custom_example_input, target)
        else:
            # Default example in case of moving to the custom tab, but not submitted yet
            custom_example_input = [5, 8, 3, 6, 7]
            target = 9

    # Generate the example and steps
    title, code, example_values, examples, methods, anchor = twoSum.get_template_values(
        example=example_in,
        custom_example_input=custom_example_input,
        target=target,
        method=method
    )

    # Pull steps from the example_values
    steps = example_values["steps"]
    # examples length is needed for enumerating through values
    examples_length = len(examples)
    # Input length is needed for enumerating through values
    input_length = len(example_values["input"])
    # Get the length of the steps for enumerating through values
    length = len(steps)
    # Check to make sure the id is within the bounds of the steps
    if id < 1 or id > length:
        abort(404)
    # Get the specific step requested
    step = steps[id - 1]
    return render_template(
        "algorithms/leetCode/array.html", 
        title=title, 
        code=code, 
        id=id, 
        length=length, 
        step=step, 
        example=example, 
        example_values=example_values,
        examples_length=examples_length,
        input_length=input_length,
        custom_example_input=custom_example_input,
        target=target,
        methods=methods,
        anchor=anchor,
        method=method
    )

@bp.route("add-two-numbers/method/<string:method>/example/<int:example>/step/<int:id>")
@bp.route("add-two-numbers/method/<string:method>/example/custom/step/<int:id>", methods=["GET", "POST"])
@bp.route("add-two-numbers/method/<string:method>/example/custom/step/<int:id>/<string:custom_example_input>", methods=["GET", "POST"])
def addTwoNumbers(id=1, example=None, custom_example_input=None, method=None):
    method = "Enumerate"

    if request.method == 'POST':
        # Post implies a custom example
        id = 1
        custom_example_input = {
            "L1": request.form['l1Input'],
            "L2": request.form['l2Input']
        }
        # Form data is brought in as a string, so we need to format it for int and list values
        custom_example_input = format_custom_example_input_and_target_add_two_numbers(custom_example_input)
    else:
        if example is not None:
            # If example is not None and either id or example are less than 1 then the url does not exist
            if example < 1 or id < 1:
                abort(404)
        elif custom_example_input is not None:
            # custom example data can still be brought in through url parameters. These also need to be formatted
            custom_example_input = json.loads(custom_example_input.replace("'", '"'))
        else:
            # Default example in case of moving to the custom tab, but not submitted yet
            custom_example_input = {
                "L1": [5, 8, 3, 6, 7],
                "L2": [6, 7, 8, 1, 4]
            }


    # Example does not need to be passed in, if it is passed in subtract one for the index
    example_in = example - 1 if example is not None else None
    title, code, example_values, examples, methods, anchor = AddTwoNumbersImplementer().get_template_values(
        example=example_in,
        custom_example_input=custom_example_input
    )

    # Pull steps from the example_values
    steps = example_values["steps"]
    # examples length is needed for enumerating through values
    examples_length = len(examples)
    # Input length is needed for enumerating through values
    input_l1_length = len(example_values["input"]["L1"])
    input_l2_length = len(example_values["input"]["L2"])
    # Get the length of the steps for enumerating through values
    length = len(steps)
    # Check to make sure the id is within the bounds of the steps
    if id < 1 or id > length:
        abort(404)
    # Get the specific step requested
    step = steps[id - 1]
    
    values_arr_length = len(step["values_arr"])

    return render_template(
        "algorithms/leetCode/addTwoNumbers.html", 
        title=title, 
        code=code, 
        id=id, 
        length=length, 
        step=step, 
        example=example, 
        example_values=example_values,
        examples_length=examples_length,
        url="algorithms.twoSum",
        input_l1_length=input_l1_length,
        input_l2_length=input_l2_length,
        custom_example_input=custom_example_input,
        target=None,
        methods=methods,
        anchor=anchor,
        method=method,
        input_l1 = example_values["input"]["L1"],
        input_l2 = example_values["input"]["L2"],
        values_arr_length=values_arr_length
    )

def format_custom_example_input(custom_example_input):
    # Format the custom example input for the algorithm
    custom_example_input = custom_example_input.replace(" ", "").replace("[", "").replace("]", "").split(",")
    custom_example_input = [int(i) for i in custom_example_input]
    return custom_example_input

def format_custom_example_input_and_target(custom_example_input, target):
    # Format the custom example input and target for the algorithm
    custom_example_input = format_custom_example_input(custom_example_input)
    target = int(target)
    return custom_example_input, target

def format_custom_example_input_and_target_add_two_numbers(custom_example_input):
    # Format the custom example input and target for the algorithm
    custom_example_input["L1"] = format_custom_example_input(custom_example_input["L1"])
    custom_example_input["L2"] = format_custom_example_input(custom_example_input["L2"])
    return custom_example_input