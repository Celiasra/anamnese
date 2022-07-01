from flask import Flask
import os
import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "database.db"))

app = Flask('__name__')
app.config['SECRET_KEY'] = 'your secret key'
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Aluno(db.Model):
    __tablename__ = 'aluno'
    ra = db.Column(db.Integer, primary_key=True)
    nome_aluno = db.Column(db.String(60), nullable=False)
    nascimento = db.Column(db.Integer)
    num_ser = db.Column(db.String(15))
    turma = db.Column(db.String(10))
    sexo = db.Column(db.String(10))
    situacao = db.Column(db.String(10))
    nome_mae = db.Column(db.String(60))
    profissao_mae = db.Column(db.String(40))
    localtrab_mae = db.Column(db.String(40))
    nasc_mae = db.Column(db.Integer)
    fone_mae = db.Column(db.Integer)
    nome_pai = db.Column(db.String(60))
    profissao_pai = db.Column(db.String(40))
    localtrab_pai = db.Column(db.String(40))
    nasc_pai = db.Column(db.Integer)
    fone_pai = db.Column(db.Integer)
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    id_anamnese_res = db.relationship('AnamneseResponsavel')
    id_anamnese_rel = db.relationship('AnamneseRelFamiliar')
    id_anamnese_pri = db.relationship('AnamnesePrimeirosAnos')
    id_anamnese_dia = db.relationship('AnamneseDiaDia')
    id_anamnese_vid = db.relationship('AnamneseVidaSocial')
    id_anamnese_viv = db.relationship('AnamneseVivPessoal')
    id_anamnese_ali = db.relationship('AnamneseAlimentacao')
    id_anamnese_son = db.relationship('AnamneseSono')
    id_anamnese_sau = db.relationship('AnamneseSaude')
    id_anamnese_psi = db.relationship('AnamneseDesPsicomotor')
    id_anamnese_rea = db.relationship('AnamneseReacEmocionais')
    id_anamnese_obs = db.relationship('AnamneseObsFinais')


class AnamneseResponsavel(db.Model):
    __tablename__ = 'anam_responsavel'
    id_anamnese_res = db.Column(db.Integer, primary_key=True)
    resp_nome = db.Column(db.String(60))
    resp_grau_par = db.Column(db.String(20))
    resp_fone_contato = db.Column(db.Integer)
    resp_resp_val = db.Column(db.String(3))
    resp_reside = db.Column(db.String(40))
    resp_tem_irm = db.Column(db.String(3))
    resp_quantos = db.Column(db.Integer)
    resp_tem_anim = db.Column(db.String(3))
    resp_qual = db.Column(db.String(40))
    resp_pais_sep = db.Column(db.String(3))
    resp_qto_tempo = db.Column(db.String(20))
    ra = db.Column(db.Integer, ForeignKey('aluno.ra'))


class AnamneseRelFamiliar(db.Model):
    __tablename__ = 'anam_rel_familiar'
    id_anamnese_rel = db.Column(db.Integer, primary_key=True)
    rel_fam_momento = db.Column(db.String(40))
    rel_fam_ativ_mae = db.Column(db.String(80))
    rel_fam_ativ_pai = db.Column(db.String(80))
    rel_fam_rel_irmaos = db.Column(db.String(80))
    rel_fam_cuidados_outros = db.Column(db.String(80))
    ra = db.Column(db.Integer, ForeignKey('aluno.ra'))


class AnamnesePrimeirosAnos(db.Model):
    __tablename__ = 'anam_primeiros_anos'
    id_anamnese_pri = db.Column(db.Integer, primary_key=True)
    prim_anos_condicoes = db.Column(db.String(80))
    prim_anos_espacos = db.Column(db.String(80))
    ra = db.Column(db.Integer, ForeignKey('aluno.ra'))


class AnamneseDiaDia(db.Model):
    __tablename__ = 'anam_dia_dia'
    id_anamnese_dia = db.Column(db.Integer, primary_key=True)
    dia_dia_horas_dormir = db.Column(db.Integer())
    dia_dia_horas_acordar = db.Column(db.Integer())
    dia_dia_faz_ativ = db.Column(db.String(3))
    dia_dia_quais = db.Column(db.String(80))
    dia_dia_qtas_vezes = db.Column(db.Integer)
    dia_dia_brinca_so = db.Column(db.String(3))
    dia_dia_com_quem = db.Column(db.String(40))
    dia_dia_cont_elet = db.Column(db.String(3))
    dia_dia_elet_quais = db.Column(db.String(40))
    dia_dia_org_brinq = db.Column(db.String(3))
    dia_dia_hab_leitura = db.Column(db.String(10))
    dia_dia_ouvir_mus = db.Column(db.String(10))
    dia_dia_tipo_mus = db.Column(db.String(40))
    dia_dia_rotina = db.Column(db.String(80))
    ra = db.Column(db.Integer, ForeignKey('aluno.ra'))


class AnamneseVidaSocial(db.Model):
    __tablename__ = 'anam_vida_social'
    id_anamnese_vid = db.Column(db.Integer, primary_key=True)
    vs_lazer = db.Column(db.String(80))
    vs_iter_loc_publico = db.Column(db.String(80))
    vs_iter_casa = db.Column(db.String(80))
    ra = db.Column(db.Integer, ForeignKey('aluno.ra'))


class AnamneseVivPessoal(db.Model):
    __tablename__ = 'anam_viv_pessoal'
    id_anamnese_viv = db.Column(db.Integer, primary_key=True)
    vp_medos = db.Column(db.String(3))
    vp_quais_medos = db.Column(db.String(80))
    vp_quais_atit = db.Column(db.String(80))
    vp_trauma = db.Column(db.String(3))
    vp_trauma_quais = db.Column(db.String(80))
    ra = db.Column(db.Integer, ForeignKey('aluno.ra'))


class AnamneseAlimentacao(db.Model):
    __tablename__ = 'anam_alimentacao'
    id_anamnese_ali = db.Column(db.Integer, primary_key=True)
    al_amamentou = db.Column(db.String(3))
    al_restricao = db.Column(db.String(3))
    al_quais = db.Column(db.String(80))
    ra = db.Column(db.Integer, ForeignKey('aluno.ra'))


class AnamneseSono(db.Model):
    __tablename__ = 'anam_sono'
    id_anamnese_son = db.Column(db.Integer, primary_key=True)
    sono_divide_quarto = db.Column(db.String(3))
    sono_divide_com_quem = db.Column(db.String(40))
    sono_dorme_dia = db.Column(db.String(3))
    sono_tem_rotina = db.Column(db.String(3))
    sono_qual_rotina = db.Column(db.String(80))
    sono_como_e = db.Column(db.String(40))
    ra = db.Column(db.Integer, ForeignKey('aluno.ra'))


class AnamneseSaude(db.Model):
    __tablename__ = 'anam_saude'
    id_anamnese_sau = db.Column(db.Integer, primary_key=True)
    saude_tem_questao = db.Column(db.String(3))
    saude_relate = db.Column(db.String(80))
    saude_cirurgia = db.Column(db.String(3))
    saude_ciruria_qual = db.Column(db.String(80))
    saude_acidente = db.Column(db.String(3))
    saude_acidente_como_foi = db.Column(db.String(80))
    saude_doencas_inf = db.Column(db.String(80))
    saude_alergia = db.Column(db.String(3))
    saude_alergia_qual = db.Column(db.String(80))
    saude_alergia_proc = db.Column(db.String(80))
    saude_alergia_fam = db.Column(db.String(3))
    saude_alergia_fam_qual = db.Column(db.String(80))
    saude_convulsao = db.Column(db.String(3))
    saude_convulsao_sit = db.Column(db.String(80))
    saude_otite = db.Column(db.String(3))
    saude_otite_freq = db.Column(db.String(80))
    saude_audiom = db.Column(db.String(3))
    saude_audiom_qdo = db.Column(db.Integer)
    saude_audiom_alter = db.Column(db.String(3))
    saude_audiom_grav = db.Column(db.String(80))
    saude_exam_oft = db.Column(db.String(3))
    saude_exam_oft_qdo = db.Column(db.Integer)
    saude_exam_oft_alt = db.Column(db.String(3))
    saude_exam_oft_grav = db.Column(db.String(80))
    ra = db.Column(db.Integer, ForeignKey('aluno.ra'))


class AnamneseDesPsicomotor(db.Model):
    __tablename__ = 'anam_des_psicomotor'
    id_anamnese_psi = db.Column(db.Integer, primary_key=True)
    psi_gestacao = db.Column(db.String(80))
    psi_engatinhou = db.Column(db.String(3))
    psi_qdo_engatinhou = db.Column(db.String(80))
    psi_como_e = db.Column(db.String(80))
    psi_aspectos = db.Column(db.String(80))
    psi_atend_fora_escola = db.Column(db.String(3))
    psi_atend_fora_escola_qual = db.Column(db.String(80))
    ra = db.Column(db.Integer, ForeignKey('aluno.ra'))


class AnamneseReacEmocionais(db.Model):
    __tablename__ = 'anam_reac_emocionais'
    id_anamnese_rea = db.Column(db.Integer, primary_key=True)
    rea_emo_carac_marc = db.Column(db.String(80))
    rea_emo_obj_efet = db.Column(db.String(3))
    rea_emo_obj_efet_sit = db.Column(db.String(80))
    rea_emo_rel_pai = db.Column(db.String(80))
    rea_emo_rel_mae = db.Column(db.String(80))
    rea_emo_rel_avos = db.Column(db.String(80))
    rea_emo_rel_cuid = db.Column(db.String(80))
    ra = db.Column(db.Integer, ForeignKey('aluno.ra'))


class AnamneseObsFinais(db.Model):
    __tablename__ = 'anam_obs_finais'
    id_anamnese_obs = db.Column(db.Integer, primary_key=True)
    obs_finais = db.Column(db.String(80))
    ra = db.Column(db.Integer, ForeignKey('aluno.ra'))
