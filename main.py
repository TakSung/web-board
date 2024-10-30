from flask import Flask, render_template, redirect, url_for,request
from datetime import datetime
from dataclasses import dataclass

app = Flask(__name__)

# class Post:
#     def __init__(self, post_id, title, content, user_id):
#         self.post_id = post_id
#         self.title = title
#         self.content = content
#         self.create_time = datetime.now()
#         self.update_time = datetime.now()
#         self.user_id = user_id

@dataclass
class Post:
    id:int
    title:str
    content:str
    user_id:str
    create_time:datetime = datetime.now()
    update_time:datetime = datetime.now()
    
@dataclass
class User:
    id:int
    account:str
    name:str
    pw:str
    
@dataclass
class Comment:
    id:int
    post_id:int
    content:str
    user_id:str
    create_time:datetime = datetime.now()
    update_time:datetime = datetime.now()

# 샘플 데이터
posts = [
    Post(id=1, title="첫 번째 게시물", content="이것은 첫 번째 게시물입니다.", user_id=1),
    Post(id=2, title="두 번째 게시물", content="이것은 두 번째 게시물입니다.", user_id=2),
]

users = [
    User(id=1, account="test1", name="이탁균", pw="123"),
    User(id=2, account="test2", name="정우성", pw="456")
]

@app.route('/')
def index():
    return redirect(url_for("get_post_list"))

@app.route('/post/<int:post_id>', methods=['GET'])
def get_post_detail(post_id):
    post = posts[post_id]
    return render_template('post_detail.html', post=post)

@app.route('/post/create', methods=['GET'])
def get_post_create():
    return render_template('post_create.html')

@app.route('/post', methods=['GET'])
def get_post_list():
    return render_template('post_list.html', posts=posts)

@app.route('/post/create', methods=['POST'])
def create_post():
    print(request)
    print(request.form)
    title = request.form['title']
    content = request.form['content']
    user_id = request.form['user_id']
    post_id = len(posts) + 1
    new_post = Post(post_id, title, content, user_id)
    posts.append(new_post)
    return redirect(url_for("index"))

@app.route('/post/edit', methods=['POST'])
def edit_post():
    print(request)
    print(request.form)
    title = request.form['title']
    content = request.form['content']   
    id = request.form['postId']
    print(id, title,content)
    post_id = len(posts) + 1
    user_id = request.form['user_id']
    new_post = Post(post_id, title, content,user_id)
    posts.append(new_post)
    return redirect(url_for("index"))

if __name__ == '__main__':
    app.run(debug=True)