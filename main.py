from flask import Flask, render_template, redirect, url_for,request
from datetime import datetime

app = Flask(__name__)

class Post:
    def __init__(self, post_id, title, content, user_id):
        self.post_id = post_id
        self.title = title
        self.content = content
        self.create_time = datetime.now()
        self.update_time = datetime.now()
        self.user_id = user_id

# 샘플 데이터
posts = [
    Post(1, "첫 번째 게시물", "이것은 첫 번째 게시물입니다.", 1),
    Post(2, "두 번째 게시물", "이것은 두 번째 게시물입니다.", 2)
]

@app.route('/')
def index():
    return redirect(url_for("get_post_list"))

@app.route('/post/<int:post_id>', methods=['GET'])
def get_post_detail(post_id):
    post = posts[post_id]
    return render_template('post_detail.html', post=post)

@app.route('/post', methods=['GET'])
def get_post_list():
    return render_template('post_list.html', posts=posts)

@app.route('/post', methods=['POST'])
def create_post():
    title = request.form['title']
    content = request.form['content']
    user_id = request.form['user_id']
    post_id = len(posts) + 1
    new_post = Post(post_id, title, content, user_id)
    posts.append(new_post)
    return redirect(url_for("index"))

if __name__ == '__main__':
    app.run(debug=True)
