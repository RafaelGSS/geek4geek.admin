from src.base.base import db
import datetime


class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)

    display_name = db.Column(db.String(255), nullable=False)
    full_name = db.Column(db.String(255), nullable=False)
    unique_name = db.Column(db.String(255), unique=True, nullable=False)
    display_description = db.Column(db.String(255), nullable=False)
    full_description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float(precision=10, scale=2, as_decimal=True), nullable=False)
    stock = db.Column(db.Integer(), nullable=False)
    display_image = db.Column(db.String(255), nullable=False)
    low_display_image = db.Column(db.String(255), nullable=True)
    big_display_image = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime(), nullable=True, default=datetime.datetime.utcnow)
