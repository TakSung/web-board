from flask import Flask, render_template, redirect, url_for,request
from datetime import datetime
from dataclasses import dataclass
import typing

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
    2: User(id=2, account="test2", name="이탁균", pw="456"),
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

@app.route('/')
def index():
    return redirect(url_for("get_post_list"))

@app.route('/post/<int:post_id>', methods=['GET'])
def get_post_detail(post_id:int):
    post = posts[post_id]
    new_comment = get_comment_list(post_id)
    return render_template('post_detail.html', post=post, comments=new_comment)


@app.route('/post/create', methods=['GET'])
def get_post_create():
    return render_template('post_create.html')

@app.route('/post', methods=['GET'])
def get_post_list():
    return render_template('post_list.html', posts=posts)

@app.route('/post/create', methods=['POST'])
def create_post():
    global post_num
    print(request)
    print(request.form)
    title = request.form['title']
    content = request.form['content']
    user_id = request.form['user_id']
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
    id = request.form['postId']
    print(id, title,content)
    user_id = request.form['user_id']
    new_post = Post(int(id), title, content,user_id)
    posts[int(id)] = new_post
    return redirect(url_for("index"))

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
