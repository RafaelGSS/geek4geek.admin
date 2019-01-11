from flask import jsonify, Response, request, Blueprint, render_template
from src.base.base import db
from src.models.product import Product


bp = Blueprint('web',  __name__)


@bp.route('/admin', methods=['GET'])
def index():
    return render_template('admin/index.html')


@bp.route('/admin/products')
def products():
    data = Product.query.all()
    print(data)
    return render_template('admin/products/list.html', products=data)