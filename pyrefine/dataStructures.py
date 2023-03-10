from flask import Blueprint, render_template
from pyrefine.StackImplementer import StackImplementer
from pyrefine.CodeFormatter import format_code 

bp = Blueprint("data-structures", __name__, url_prefix="/data-structures")

@bp.route("stack/example/<int:id>")
def stack(id):
    stack = StackImplementer()
    title, description, code, examples = stack.get_template_values()
    example = examples[id - 1]
    length = len(examples)
    return render_template("dataStructures/stack.html", title=title, description=description, code=code, example=example, length=length, id=id)