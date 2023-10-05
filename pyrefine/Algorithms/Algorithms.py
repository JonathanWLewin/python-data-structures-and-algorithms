from flask import Blueprint, render_template, abort
from pyrefine.Algorithms.TwoSum.TwoSumImplementer import TwoSumImplementer

bp = Blueprint("algorithms", __name__, url_prefix="/algorithms")

@bp.route("two-sum/step/<int:id>")
def twoSum(id):
    twoSum = TwoSumImplementer()
    title, code = twoSum.get_template_values()
    return render_template("algorithms/baseAlgorithm.html", title=title, code=code, id=id, length=10, implementations={'test': 'test1', 'test2': 'test3'})