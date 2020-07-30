"""Flask app for Cupcakes"""
from flask import Flask, request, jsonify, render_template, redirect
from models import db, connect_db, Cupcake
from forms import AddCupcakeForm, UpdateCupcakeForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "oneonetwotwo"

connect_db(app)


@app.route('/')
def home():
    #cupcakes = Cupcake.query.all()
    form = AddCupcakeForm()
    update_form = UpdateCupcakeForm()
    return render_template('index.html', form=form, update_form=update_form)


@app.route('/api/cupcakes')
def show_all_cupcakes():
    cupcakes = Cupcake.query.all()
    all_cupcakes = [cupcake.serialize() for cupcake in cupcakes]
    return jsonify(cupcakes=all_cupcakes)


@app.route('/api/cupcakes', methods=["POST"])
def create_cupcake():
    new_cupcake = Cupcake(flavor=request.json["flavor"], size=request.json["size"],
                          rating=request.json["rating"], image=request.json["image"] or None)
    db.session.add(new_cupcake)
    db.session.commit()
    return (jsonify(cupcake=new_cupcake.serialize()), 201)


@app.route('/api/cupcakes/<int:id>')
def get_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    return jsonify(cupcake=cupcake.serialize())


@app.route('/api/cupcakes/<int:id>', methods=["PATCH"])
def update_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    cupcake.flavor = request.json.get("flavor", cupcake.flavor)
    cupcake.size = request.json.get("size", cupcake.size)
    cupcake.rating = request.json.get("rating", cupcake.rating)
    cupcake.image = request.json.get("image", cupcake.image)
    db.session.commit()
    return jsonify(cupcake=cupcake.serialize())


@app.route('/api/cupcakes/<int:id>', methods=["DELETE"])
def delete_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(message="Deleted")


# @app.route('/update/cupcakes/<int:id>', methods=["GET", "POST"])
# def update(id):
#     cupcake = Cupcake.query.get_or_404(id)
#     form = AddCupcakeForm(obj=cupcake)
#     if form.validate_on_submit():
#         """update the cupcake data if this is a POST request"""
#         cupcake.flavor = form.flavor.data
#         cupcake.size = form.size.data
#         cupcake.rating = form.rating.data
#         cupcake.image = form.image.data

#         db.session.commit()
#         return redirect('/')
#     else:
#         """render pet_info.html for showing pet detail and editting form if this is a GET request"""
#         return render_template('cupcake_update.html', form=form, cupcake=cupcake)
