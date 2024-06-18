from flask import render_template, request, redirect, url_for, Blueprint
from services.posts_service import PostsService

posts_blueprint = Blueprint('posts', __name__)
posts_service = PostsService()

@posts_blueprint.route("/")
def index():
    posts = posts_service.get_posts()
    return render_template('index.html', posts=posts)

@posts_blueprint.route('/new_post', methods=['GET','POST'])
def upload_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        author = request.form['author']
        posts_service.new_post((title, content, author))
        return redirect(url_for('posts.index'))
    return render_template('create.html')

@posts_blueprint.route('/update/<int:index>', methods=['GET','POST'])
def update_post(index):
    post = posts_service.get_one(index)
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        author = request.form['author']
        posts_service.update_post((title, content, author, index))
        
        return redirect(url_for('posts.index'))
    return render_template('update.html', post=post)
    

@posts_blueprint.route("/delete/<int:index>")
def delete_post(index):
    posts_service.delete_post(index)
    return redirect(url_for('posts.index'))