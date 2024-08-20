from flask import Flask, request, jsonify
from flask_cors import CORS
import random
from typing import List, Tuple

app = Flask(__name__)
CORS(app)

class MazeGenerator:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.maze = [[1 for _ in range(width)] for _ in range(height)]
        
    def generate(self):
        self._carve_path(0, 0)
        
    def _carve_path(self, x: int, y: int):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        random.shuffle(directions)
        
        for dx, dy in directions:
            nx, ny = x + dx*2, y + dy*2
            if 0 <= nx < self.width and 0 <= ny < self.height and self.maze[ny][nx] == 1:
                self.maze[y+dy][x+dx] = 0
                self.maze[ny][nx] = 0
                self._carve_path(nx, ny)
    
    def add_crossings(self, num_crossings: int):
        for _ in range(num_crossings):
            x = random.randint(1, self.width-2)
            y = random.randint(1, self.height-2)
            if self.maze[y][x] == 1:
                self.maze[y][x] = 0

def solve_maze(maze: List[List[int]], start: Tuple[int, int], end: Tuple[int, int]) -> List[Tuple[int, int]]:
    def dfs(x: int, y: int, path: List[Tuple[int, int]]) -> List[Tuple[int, int]] | None:
        if (x, y) == end:
            return path
        
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(maze[0]) and 0 <= ny < len(maze) and maze[ny][nx] == 0 and (nx, ny) not in path:
                result = dfs(nx, ny, path + [(nx, ny)])
                if result:
                    return result
        return None
    
    return dfs(start[0], start[1], [start])

@app.route('/generate-maze', methods=['POST'])
def generate_maze():
    data = request.json
    width = data.get('width', 21)
    height = data.get('height', 21)
    crossings = data.get('crossings', 5)
    
    generator = MazeGenerator(width, height)
    generator.generate()
    generator.add_crossings(crossings)
    
    return jsonify({'maze': generator.maze})

@app.route('/solve-maze', methods=['POST'])
def solve_maze_route():
    data = request.json
    maze = data.get('maze')
    start = tuple(data.get('start', [0, 0]))
    end = tuple(data.get('end', [len(maze[0])-1, len(maze)-1]))
    
    solution = solve_maze(maze, start, end)
    
    return jsonify({'solution': solution})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)