import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO aluno (nome_aluno, nascimento, num_ser, turma, sexo, situacao, nome_mae, profissao_mae, "
            "localtrab_mae, nasc_mae, fone_mae, nome_pai, profissao_pai, localtrab_pai, nasc_pai, fone_pai) "
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            ('Fulano da Silva', '19032016', '1 ano', 'turma A', 'Masculino', 'Adotivo', 'Maria da Silva',
             'Recepcionista', 'Hospital Geral Pirajussara', '19031976', '11999999999', 'Jose da Silva',
             'Motorista', 'Viação Pirajussara', '19031975', '1199999999')
            )

cur.execute("INSERT INTO aluno (nome_aluno, nascimento, num_ser, turma, sexo, situacao, nome_mae, profissao_mae, "
            "localtrab_mae, nasc_mae, fone_mae, nome_pai, profissao_pai, localtrab_pai, nasc_pai, fone_pai) "
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            ('Ciclano da Silva', '19032016', '2 ano', 'turma A', 'Masculino', 'Adotivo', 'Maria da Silva',
             'Recepcionista', 'Hospital Geral Pirajussara', '19031976', '11999999999', 'Jose da Silva',
             'Motorista', 'Viação Pirajussara', '19031975', '1199999999')
            )

cur.execute("INSERT INTO aluno (nome_aluno, nascimento, num_ser, turma, sexo, situacao, nome_mae, profissao_mae, "
            "localtrab_mae, nasc_mae, fone_mae, nome_pai, profissao_pai, localtrab_pai, nasc_pai, fone_pai) "
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            ('Beltrano da Silva', '19032016', '3 ano', 'turma A', 'Masculino', 'Adotivo', 'Maria da Silva',
             'Recepcionista', 'Hospital Geral Pirajussara', '19031976', '11999999999', 'Jose da Silva',
             'Motorista', 'Viação Pirajussara', '19031975', '1199999999')
            )

connection.commit()
connection.close()
