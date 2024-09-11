from app.books import book_blueprint
from app.models import Book , db
from werkzeug.utils import secure_filename
from flask import render_template, request, redirect, url_for, flash
import os



@book_blueprint.route('', endpoint='index')
def index():
    books = Book.query.all()
    return render_template("books/index.html", books=books)

#--------------------------------------------------------------------------------------------------

@book_blueprint.route("<int:id>", endpoint="show")
def show(id):
    book = db.get_or_404(Book, id)
    return  render_template("books/show.html", book=book)

#------------------------------------------------------------------------------------------------------

@book_blueprint.route("create", endpoint="create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        book = Book(title=request.form["title"],num_of_pages=request.form["num_of_pages"] ,image=request.form["image"] , description=request.form["description"], )
        db.session.add(book)
        db.session.commit()
        return redirect(url_for("books.index"))


    return render_template("books/create.html")

#-----------------------------------------------------------------------------------------------------------
from app.books.forms import BookForm



@book_blueprint.route("form/create", endpoint="form_create", methods=["POST", "GET"])
def create_book():
    form  = BookForm()
    if request.method=='POST':
        if form.validate_on_submit():
            image_name=None
            if request.files.get('image'):
                image= form.image.data
                image_name =secure_filename(image.filename)
                # save image to server
                image.save(os.path.join('app/static/books/images/', image_name))
                
            data= dict(request.form)
            del data['csrf_token']
            del data['submit']
            # save image name
            data["image"]= image_name
            #print(request.form)
            book= Book(**data)
            db.session.add(book)
            db.session.commit()
            return redirect(url_for("books.index"))



    return  render_template("books/forms/create.html", form=form)

#-------------------------------------------------------------------------------------------------------

@book_blueprint.route("/form/edit/<int:book_id>", endpoint="form_edit", methods=["GET", "POST"])
def edit_book(book_id):

    book = Book.query.get_or_404(book_id)
    
    form = BookForm(obj=book)
    
    if request.method == 'POST':
        if form.validate_on_submit():

            data = dict(request.form)
            del data['csrf_token']
            del data['submit']

            # if image updated
            if request.files.get('image'):
                image = form.image.data
                image_name = secure_filename(image.filename)
                #save to server
                image.save(os.path.join('app/static/books/images/', image_name))
                #save name
                data['image'] = image_name  
            else:

                data['image'] = book.image
            
  
            for key, value in data.items():
                setattr(book, key, value)
            
            db.session.commit()
            return redirect(url_for("books.index"))
    
    return render_template("books/forms/edit.html", form=form, book=book)

#----------------------------------------------------------------------------------

@book_blueprint.route("/delete/<int:book_id>", methods=["POST"])
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('books.index'))