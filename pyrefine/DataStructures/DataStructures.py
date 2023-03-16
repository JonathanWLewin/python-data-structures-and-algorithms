from flask import Blueprint, render_template, abort
from pyrefine.DataStructures.Stack.StackImplementer import StackImplementer
from pyrefine.DataStructures.LinkedList.LinkedListImplementor import LinkedListImplementor

bp = Blueprint("data-structures", __name__, url_prefix="/data-structures")

@bp.route("stack/example/<int:id>")
def stack(id):
    stack = StackImplementer()
    title, code, examples = stack.get_template_values()
    length = len(examples)
    if id < 1 or id > length:
        abort(404)
    example = examples[id - 1]
    return render_template("dataStructures/stack.html", title=title, code=code, example=example, length=length, id=id)

@bp.route("linkedlist/example/<int:id>")
def linked_list(id):
    lst = LinkedListImplementor()
    title, code, examples = lst.get_template_values()
    length = len(examples)
    if id < 1 or id > length:
        abort(404)
    example = examples[id - 1]
    return render_template("dataStructures/linkedList.html", title=title, code=code, example=example, length=length, id=id)