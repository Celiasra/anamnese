from flask import render_template, request, url_for, redirect, flash, jsonify
from werkzeug.exceptions import abort
from models import db


# FUNÇÃO GET ALUNO
def get_aluno(Aluno, ra):
    aluno = Aluno.query.filter_by(ra=ra).first()
    if aluno is None:
        abort(484)
    return aluno

def ViewsAluno(app, Aluno):
    pass

# ROTA PARA A PAGINA DE CONSULTA ALUNO
    @app.route('/pesquisar_aluno')
    def pesquisar_aluno():
        lista_alunos = Aluno.query.all()
        return render_template('Aluno/pesquisar_aluno.html', alunos=lista_alunos)

    @app.route('/create', methods=('GET', 'POST'))
    def create():
        if request.method == 'POST':
            nome_aluno = request.form['nome_aluno']
            nascimento = request.form['nascimento']
            num_ser = request.form['num_ser']
            turma = request.form['turma']
            sexo = request.form['sexo']
            situacao = request.form['situacao']
            nome_mae = request.form['nome_mae']
            profissao_mae = request.form['profissao_mae']
            localtrab_mae = request.form['localtrab_mae']
            nasc_mae = request.form['nasc_mae']
            fone_mae = request.form['fone_mae']
            nome_pai = request.form['nome_pai']
            profissao_pai = request.form['profissao_pai']
            localtrab_pai = request.form['localtrab_pai']
            nasc_pai = request.form['nasc_pai']
            fone_pai = request.form['fone_pai']

            if not nome_aluno or not nascimento:
                flash('O Nome e nascimento são Obrigatórios!')
            else:
                aluno = Aluno(nome_aluno=nome_aluno, nascimento=nascimento, num_ser=num_ser, turma=turma, sexo=sexo,
                              situacao=situacao, nome_mae=nome_mae, profissao_mae=profissao_mae,
                              localtrab_mae=localtrab_mae, nasc_mae=nasc_mae, fone_mae=fone_mae, nome_pai=nome_pai,
                              profissao_pai=profissao_pai, localtrab_pai=localtrab_pai, nasc_pai=nasc_pai,
                              fone_pai=fone_pai)
                db.session.add(aluno)
                db.session.commit()
                return redirect(url_for('pesquisar_aluno'))
        return render_template('Aluno/cadastrar_aluno.html')


# ROTA PARA A PAGINA DE CONSULTA ALUNO
    @app.route('/<int:ra>')
    def detalhe_aluno(ra):
        detalhe = get_aluno(Aluno, ra)
        return render_template('Aluno/consultar_aluno.html', detalhe_aluno=detalhe)

