from flask import Flask, render_template, redirect, url_for,request
from datetime import datetime
from dataclasses import dataclass
from math import ceil
from copy import copy
import typing

app = Flask(__name__)

@dataclass
class Post:
    id:int
    title:str
    content:str
    user_id:int
    user_name:str=""
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
    user_id:int
    create_time:datetime = datetime.now()
    update_time:datetime = datetime.now()
    
@dataclass
class CommentDto:
    id:int
    post_id:int
    content:str
    user:str
    create_time:datetime
    update_time:datetime

# 샘플 데이터
posts = {
    1: Post(id=1, title="첫 번째 게시물", content="이것은 첫 번째 게시물입니다.", user_id=1),
    2: Post(id=2, title="두 번째 게시물", content="이것은 두 번째 게시물입니다.", user_id=2),
    3: Post(id=3, title="세 번째 게시물", content="이것은 세 번째 게시물입니다.", user_id=3),
    4: Post(id=4, title="네 번째 게시물", content="이것은 네 번째 게시물입니다.", user_id=4),
    5: Post(id=5, title="다섯 번째 게시물", content="이것은 다섯 번째 게시물입니다.", user_id=5),
    6: Post(id=6, title="여섯 번째 게시물", content="이것은 여섯 번째 게시물입니다.", user_id=6),
}

users = {
    1: User(id=1, account="test1", name="정우성", pw="123"),
    2: User(id=2, account="test1", name="이탁균", pw="123"),
    3: User(id=3, account="test1", name="김철수", pw="123"),
    4: User(id=4, account="test1", name="김영희", pw="123"),
    5: User(id=5, account="test2", name="김대청", pw="456"),
    6: User(id=6, account="test2", name="김대치", pw="456"),
}

comments = {
    1: Comment(id=1, post_id=1, content="오 대박 첫글에 첫번째 댓글 남기고 갑니다.",    user_id=2),
    2: Comment(id=2, post_id=1, content="대박이라니... 틀딱 냄새남",                user_id=1),
    3: Comment(id=3, post_id=1, content="... 그래면 요즘은 뭐라고 하는데?",          user_id=2),
    4: Comment(id=4, post_id=1, content="안 안려줄건데?",                         user_id=1),
    5: Comment(id=5, post_id=2, content="틀딱 글에 댓글 남기고 감",                 user_id=1),
    6: Comment(id=6, post_id=2, content="... 발 닦고 잠이나 자라",                 user_id=2),
}

post_num = len(posts)
user_num = len(users)
comment_num = len(comments)

@app.route('/comment/create', methods=['POST'])
def create_comment():
    global comment_num
    print(request)
    print(request.form)
    content = request.form['commentContent']
    user_id = int(request.form['userId'])
    post_id = request.form['postId']
    comment_num += 1
    comment_id = comment_num
    new_comment = Comment(
        id = comment_id,
        post_id = int(post_id),
        content = content,
        user_id = user_id
    )
    comments[comment_id] = new_comment
    print(comments)
    return redirect(url_for("index"))

@app.route('/')
def index():
    return redirect(url_for("get_post_list", page=1))

@app.route('/post/<int:post_id>', methods=['GET'])
def get_post_detail(post_id:int):
    post = posts[post_id]
    post.user_name = get_user(post.user_id).account
    new_comment = get_comment_list(post_id)
    post.user_name = get_user(post.user_id).name
    return render_template('post_detail.html', post=post, comments=new_comment)

@app.route('/post/edit/<int:post_id>', methods=['GET'])
def get_post_edit(post_id:int):
    post = posts[post_id]
    return render_template('post_edit.html', post=post)

@app.route('/post/create', methods=['GET'])
def get_post_create():
    return render_template('post_create.html')

@app.route('/post/list/<int:page>', methods=['GET'])
def get_post_list(page:int): # page 1~end
    size = 2
    max_page = ceil(len(posts) / size)
    page = min(max_page, max(page-1,0))
    start_idx = page * size
    end_idx = min(start_idx+size,  len(posts))
    new_posts = list(posts.values())[start_idx:end_idx]
    if len(new_posts) == 0:
        return redirect(url_for("get_post_list", page=page))
    else :
        return render_template('post_list.html', posts=new_posts, page=page+1)

@app.route('/post/create', methods=['POST'])
def create_post():
    global post_num
    print(request)
    print(request.form)
    title = request.form['title']
    content = request.form['content']
    user_id = int(request.form['user_id'])
    post_num += 1
    post_id = post_num
    new_post = Post(post_id, title, content, user_id)
    posts[post_id] = new_post
    return redirect(url_for("index"))

@app.route('/post/edit', methods=['POST'])
def edit_post():
    print(request)
    print(request.form)
    title = request.form['title']
    content = request.form['content']   
    post_id:int = int(request.form['postId'])
    print(post_id, title,content)
    user_id = int(request.form['user_id'])
    new_post = Post(post_id, title, content,user_id)
    posts[post_id] = new_post
    return redirect(url_for("get_post_detail", post_id=post_id))

@app.route('/post/delete/<int:post_id>', methods=['GET'])
def delete_post(post_id):
    del posts[post_id]
    return redirect(url_for("index"))

def get_comment_list(post_id:int)-> typing.List[CommentDto]:
    # return convert_to_comment_dto(comments)
    # 아래를 구현하시오
    comment_list:CommentDto = []
    for comment in comments.values():
        if comment.post_id == post_id:
            comment_list.append(convert_to_comment_dto(comment))
    return comment_list

def get_user(user_id:int) -> User:
    return users[user_id]

def convert_to_comment_dto(comment: Comment)-> CommentDto:
    return CommentDto(
                id=comment.id,
                post_id=comment.post_id,
                content=comment.content,
                user=get_user(comment.user_id).name,
                create_time=comment.create_time,
                update_time=comment.update_time,
            )
    
if __name__ == '__main__':
    app.run(debug=True)
