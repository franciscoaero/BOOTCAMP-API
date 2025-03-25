from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Initialize flask app
app = Flask(__name__)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

# Database model for students
class Aluno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)

# Database model for courses
class Curso(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)

# Create database tables if they don't exist
with app.app_context():
    db.create_all()

# ---------------------------
# STUDENT ROUTES
# ---------------------------

# Route to create a new student
@app.route('/alunos', methods=['POST'])
def cadastrar_aluno():
    dados = request.json
    novo_aluno = Aluno(nome=dados['nome'])
    db.session.add(novo_aluno)
    db.session.commit()
    return jsonify({'mensagem': 'Aluno cadastrado com sucesso!'})

# Route to list all students
@app.route('/alunos', methods=['GET'])
def listar_alunos():
    alunos = Aluno.query.all()
    return jsonify([{'id': aluno.id, 'nome': aluno.nome} for aluno in alunos])

# ---------------------------
# COURSE ROUTES
# ---------------------------

# Route to register a new course
@app.route('/cursos', methods=['POST'])
def cadastrar_curso():
    dados = request.json
    novo_curso = Curso(nome=dados['nome'])
    db.session.add(novo_curso)
    db.session.commit()
    return jsonify({'mensagem': 'Curso cadastrado com sucesso!'})

# Route to list all courses
@app.route('/cursos', methods=['GET'])
def listar_cursos():
    cursos = Curso.query.all()
    return jsonify([{'id': curso.id, 'nome': curso.nome} for curso in cursos])

# Start the development server with degub mode enabled
if __name__ == '__main__':
    app.run(debug=True)