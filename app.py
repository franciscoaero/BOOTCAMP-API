from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class Aluno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)

class Curso(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)

with app.app_context():
    db.create_all()

# Alunos
@app.route('/alunos', methods=['POST'])
def cadastrar_aluno():
    dados = request.json
    novo_aluno = Aluno(nome=dados['nome'])
    db.session.add(novo_aluno)
    db.session.commit()
    return jsonify({'mensagem': 'Aluno cadastrado com sucesso!'})

@app.route('/alunos', methods=['GET'])
def listar_alunos():
    alunos = Aluno.query.all()
    return jsonify([{'id': aluno.id, 'nome': aluno.nome} for aluno in alunos])

# Cursos
@app.route('/cursos', methods=['POST'])
def cadastrar_curso():
    dados = request.json
    novo_curso = Curso(nome=dados['nome'])
    db.session.add(novo_curso)
    db.session.commit()
    return jsonify({'mensagem': 'Curso cadastrado com sucesso!'})

@app.route('/cursos', methods=['GET'])
def listar_cursos():
    cursos = Curso.query.all()
    return jsonify([{'id': curso.id, 'nome': curso.nome} for curso in cursos])

if __name__ == '__main__':
    app.run(debug=True)
