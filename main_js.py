from flask import Flask, jsonify, request, render_template
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
    return render_template('index_js.html')

@app.route('/api/posts', methods=['GET'])
def get_posts():
    posts_data = [{
        'post_id': post.post_id,
        'title': post.title,
        'content': post.content,
        'create_time': post.create_time.strftime("%Y-%m-%d %H:%M:%S"),
        'user_id': post.user_id
    } for post in posts]
    return jsonify(posts_data)

@app.route('/api/post', methods=['POST'])
def create_post():
    data = request.get_json()
    new_post = Post(len(posts) + 1, data['title'], data['content'], data['user_id'])
    posts.append(new_post)
    return jsonify({'message': 'Post created successfully'}), 201





if __name__ == '__main__':
    app.run(debug=True)
