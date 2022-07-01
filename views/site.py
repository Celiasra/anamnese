from flask import render_template


def ViewsSite(app):
    pass

    # ROTAS RELATIVAS AO SITE =================================================#

    # ROTA PARA A PAGINA INICIAL
    @app.route('/')
    def index():
        return render_template('index.html')

    # ROTA PARA A PAGINA A ESCOLA
    @app.route('/aescola')
    def aescola():
        return render_template('Site/aescola.html', titulo='A Escola')

    # ROTA PARA A PAGINA EVENTOS E NOTÍCIAS
    @app.route('/eventos_noticias')
    def eventos_noticias():
        return render_template('Site/eventos_noticias.html', titulo='Eventos e Notícias')

    # ROTA PARA A PAGINA CONTATO
    @app.route('/contato')
    def contato():
        return render_template('Site/contato.html', titulo='Contato')

    # ROTA PARA A PAGINA ÁREA LOGADA
    @app.route('/login')
    def login():
        return render_template('login.html')
