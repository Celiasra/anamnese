DROP TABLE IF EXISTS aluno;

CREATE TABLE aluno (
    ra INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_aluno TEXT NOT NULL,
    nascimento INTEGER NOT NULL,
    num_ser TEXT,
    turma TEXT,
    sexo TEXT,
    situacao TEXT,
    nome_mae TEXT,
    profissao_mae TEXT,
    localtrab_mae TEXT,
    nasc_mae INTEGER DEFAULT 0,
    fone_mae INTEGER DEFAULT 0,
    nome_pai TEXT,
    profissao_pai TEXT,
    localtrab_pai TEXT,
    nasc_pai INTEGER DEFAULT 0,
    fone_pai INTEGER DEFAULT 0,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

DROP TABLE IF EXISTS anam_responsavel;

CREATE TABLE anam_responsavel (
    id_anamnese_res INTEGER PRIMARY KEY AUTOINCREMENT,
    resp_nome TEXT,
    resp_grau_par TEXT,
    resp_fone_contato INTEGER DEFAULT 0,
    resp_resp_val TEXT,
    resp_reside TEXT,
    resp_tem_irm TEXT,
    resp_quantos INTEGER DEFAULT 0,
    resp_tem_anim TEXT,
    resp_qual TEXT,
    resp_pais_sep TEXT,
    resp_qto_tempo INTEGER DEFAULT 0,
    ra INTEGER,
    FOREIGN KEY (ra)
        REFERENCES aluno (ra)
);


DROP TABLE IF EXISTS anam_rel_familiar;

CREATE TABLE anam_rel_familiar (
    id_anamnese_rel INTEGER PRIMARY KEY AUTOINCREMENT,
    rel_fam_momento TEXT,
    rel_fam_ativ_mae TEXT,
    rel_fam_ativ_pai TEXT,
    rel_fam_rel_irmaos TEXT,
    rel_fam_cuidados_outros TEXT,
    ra INTEGER,
    FOREIGN KEY (ra)
        REFERENCES aluno (ra)
);

DROP TABLE IF EXISTS anam_primeiros_anos;

CREATE TABLE anam_primeiros_anos (
    id_anamnese_pri INTEGER PRIMARY KEY AUTOINCREMENT,
    prim_anos_condicoes TEXT,
    prim_anos_espacos TEXT,
    ra INTEGER,
    FOREIGN KEY (ra)
        REFERENCES aluno (ra)
);

DROP TABLE IF EXISTS anam_dia_dia;

CREATE TABLE anam_dia_dia (
    id_anamnese_dia INTEGER PRIMARY KEY AUTOINCREMENT,
    dia_dia_horas_dormir INTEGER DEFAULT 0,
    dia_dia_horas_acordar INTEGER DEFAULT 0,
    dia_dia_faz_ativ TEXT,
    dia_dia_quais TEXT,
    dia_dia_qtas_vezes INTEGER DEFAULT 0,
    dia_dia_brinca_so TEXT,
    dia_dia_com_quem TEXT,
    dia_dia_cont_elet TEXT,
    dia_dia_elet_quais TEXT,
    dia_dia_org_brinq TEXT,
    dia_dia_hab_leitura TEXT,
    dia_dia_ouvir_mus TEXT,
    dia_dia_tipo_mus TEXT,
    dia_dia_rotina TEXT,
    ra INTEGER,
    FOREIGN KEY (ra)
        REFERENCES aluno (ra)
);

DROP TABLE IF EXISTS anam_vida_social;

CREATE TABLE anam_vida_social (
    id_anamnese_vid INTEGER PRIMARY KEY AUTOINCREMENT,
    vs_lazer TEXT,
    vs_iter_loc_publico TEXT,
    vs_iter_casa TEXT,
    ra INTEGER,
    FOREIGN KEY (ra)
        REFERENCES aluno (ra)
);

DROP TABLE IF EXISTS anam_viv_pessoal;

CREATE TABLE anam_viv_pessoal (
    id_anamnese_viv INTEGER PRIMARY KEY AUTOINCREMENT,
    vp_medos TEXT,
    vp_quais_medos TEXT,
    vp_quais_atit TEXT,
    vp_trauma TEXT,
    vp_trauma_quais TEXT,
    ra INTEGER,
    FOREIGN KEY (ra)
        REFERENCES aluno (ra)
);

DROP TABLE IF EXISTS anam_alimentacao;

CREATE TABLE anam_alimentacao (
    id_anamnese_ali INTEGER PRIMARY KEY AUTOINCREMENT,
    al_amamentou TEXT,
    al_restricao TEXT,
    al_quais TEXT,
    ra INTEGER,
    FOREIGN KEY (ra)
        REFERENCES aluno (ra)
);

DROP TABLE IF EXISTS anam_sono;

CREATE TABLE anam_sono (
    id_anamnese_son INTEGER PRIMARY KEY AUTOINCREMENT,
    sono_divide_quarto TEXT,
    sono_divide_com_quem TEXT,
    sono_dorme_dia TEXT,
    sono_tem_rotina TEXT,
    sono_qual_rotina TEXT,
    sono_como_e TEXT,
    ra INTEGER,
    FOREIGN KEY (ra)
        REFERENCES aluno (ra)
);

DROP TABLE IF EXISTS anam_saude;

CREATE TABLE anam_saude (
    id_anamnese_sau INTEGER PRIMARY KEY AUTOINCREMENT,
    saude_tem_questao TEXT,
    saude_relate TEXT,
    saude_cirurgia TEXT,
    saude_ciruria_qual TEXT,
    saude_acidente TEXT,
    saude_acidente_como_foi TEXT,
    saude_doencas_inf TEXT,
    saude_alergia TEXT,
    saude_alergia_qual TEXT,
    saude_alergia_proc TEXT,
    saude_alergia_fam TEXT,
    saude_alergia_fam_qual TEXT,
    saude_convulsao TEXT,
    saude_convulsao_sit TEXT,
    saude_otite TEXT,
    saude_otite_freq TEXT,
    saude_audiom TEXT,
    saude_audiom_qdo INTEGER DEFAULT 0,
    saude_audiom_alter TEXT,
    saude_audiom_grav TEXT,
    saude_exam_oft TEXT,
    saude_exam_oft_qdo INTEGER DEFAULT 0,
    saude_exam_oft_alt TEXT,
    saude_exam_oft_grav TEXT,
    ra INTEGER,
    FOREIGN KEY (ra)
        REFERENCES aluno (ra)
);

DROP TABLE IF EXISTS anam_des_psicomotor;

CREATE TABLE anam_des_psicomotor (
    id_anamnese_psi INTEGER PRIMARY KEY AUTOINCREMENT,
    psi_gestacao TEXT,
    psi_engatinhou TEXT,
    psi_qdo_engatinhou TEXT,
    psi_como_e TEXT,
    psi_aspectos TEXT,
    psi_atend_fora_escola TEXT,
    psi_atend_fora_escola_qual TEXT,
    ra INTEGER,
    FOREIGN KEY (ra)
        REFERENCES aluno (ra)
);

DROP TABLE IF EXISTS anam_reac_emocionais;

CREATE TABLE anam_reac_emocionais (
    id_anamnese_rea INTEGER PRIMARY KEY AUTOINCREMENT,
    rea_emo_carac_marc TEXT,
    rea_emo_obj_efet TEXT,
    rea_emo_obj_efet_sit TEXT,
    rea_emo_rel_pai TEXT,
    rea_emo_rel_mae TEXT,
    rea_emo_rel_avos TEXT,
    rea_emo_rel_cuid TEXT,
    ra INTEGER,
    FOREIGN KEY (ra)
        REFERENCES aluno (ra)
);

DROP TABLE IF EXISTS anam_obs_finais;

CREATE TABLE anam_obs_finais (
    id_anamnese_obs INTEGER PRIMARY KEY AUTOINCREMENT,
    obs_finais TEXT,
    ra INTEGER,
    FOREIGN KEY (ra)
        REFERENCES aluno (ra)
);