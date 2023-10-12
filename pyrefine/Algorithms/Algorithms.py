from flask import Blueprint, render_template, abort
from pyrefine.Algorithms.TwoSum.TwoSumImplementer import TwoSumImplementer

bp = Blueprint("algorithms", __name__, url_prefix="/algorithms")

@bp.route("two-sum/example/<int:example>/step/<int:id>")
def twoSum(id=1, example=1):
    twoSum = TwoSumImplementer()
    title, code, example_values, examples = twoSum.get_template_values(example - 1)
    steps = example_values["steps"]
    examples_length = len(examples)
    length = len(steps)
    if id < 1 or id > length:
        abort(404)
    step = steps[id - 1]
    return render_template(
        "algorithms/baseAlgorithm.html", 
        title=title, 
        code=code, 
        id=id, 
        length=length, 
        step=step, 
        example=example, 
        example_values=example_values,
        examples_length=examples_length,
        url="algorithms.twoSum"
    )