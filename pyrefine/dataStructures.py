from flask import Blueprint, render_template, abort
from pyrefine.StackImplementer import StackImplementer

bp = Blueprint("data-structures", __name__, url_prefix="/data-structures")

@bp.route("stack/example/<int:id>")
def stack(id):
    stack = StackImplementer()
    title, description, code, examples = stack.get_template_values()
    length = len(examples)
    if id < 1 or id > length:
        abort(404)
    example = examples[id - 1]
    return render_template("dataStructures/stack.html", title=title, description=description, code=code, example=example, length=length, id=id)