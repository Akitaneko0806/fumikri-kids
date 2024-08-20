from flask import Flask, jsonify, render_template
from maze_generator import generate_maze

app = Flask(__name__)

@app.route('/generate/<int:size>', methods=['GET'])
def generate(size):
    maze = generate_maze(size)
    return jsonify(maze)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
