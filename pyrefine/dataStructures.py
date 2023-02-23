import inspect
from flask import Blueprint, render_template

bp = Blueprint("data-structures", __name__, url_prefix="/data-structures")

def code_test():
    print("Hello")

@bp.route("list")
def list():
    return render_template("dataStructures/list.html", code=inspect.getsource(code_test))