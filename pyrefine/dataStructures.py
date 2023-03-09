from flask import Blueprint, render_template
from pyrefine.StackImplementer import StackImplementer
from pyrefine.CodeFormatter import format_code 

bp = Blueprint("data-structures", __name__, url_prefix="/data-structures")

def code_test():
    print("Hello")

@bp.route("list")
def list():
    stack = StackImplementer()
    title, description, code, examples = stack.get_template_values()
    return render_template("dataStructures/list.html", title=title, description=description, code=code, examples=examples)