from flask import render_template, redirect, url_for, request
from models import db, Aluno, AnamneseResponsavel, AnamneseRelFamiliar, AnamnesePrimeirosAnos, AnamneseDiaDia, \
    AnamneseVidaSocial, AnamneseVivPessoal, AnamneseAlimentacao, AnamneseSono, AnamneseSaude, AnamneseDesPsicomotor, \
    AnamneseReacEmocionais, AnamneseObsFinais
from views.alunos import get_aluno


def ViewsAnamnese(app):
    pass

    # ROTA PARA A PAGINA CADASTRAR ANAMNESE
    @app.route('/cadastrar_anamnese/<int:ra>')
    def cadastrar_anamnese(ra):
        aluno_cadastro = get_aluno(Aluno, ra)
        return render_template('Anamnese/cadastrar_anamnese.html', detalhe_aluno=aluno_cadastro)

    # ROTA PARA A PAGINA DO RESPONSÁVEL
    @app.route('/anam_responsavel/<int:ra>', methods=('GET', 'POST'))
    def anam_responsavel(ra):
        aluno_cadastro = get_aluno(Aluno, ra)
        if request.method == 'POST':
            resp_nome = request.form['resp_nome']
            resp_grau_par = request.form['resp_grau_par']
            resp_fone_contato = request.form['resp_fone_contato']
            resp_resp_val = request.form['resp_resp_val']
            resp_reside = request.form['resp_reside']
            resp_tem_irm = request.form['resp_tem_irm']
            resp_quantos = request.form['resp_quantos']
            resp_tem_anim = request.form['resp_tem_anim']
            resp_qual = request.form['resp_qual']
            resp_pais_sep = request.form['resp_pais_sep']
            resp_qto_tempo = request.form['resp_qto_tempo']
            anam_responsavel = AnamneseResponsavel(resp_nome=resp_nome, resp_grau_par=resp_grau_par,
                                                   resp_fone_contato=resp_fone_contato, resp_resp_val=resp_resp_val,
                                                   resp_reside=resp_reside, resp_tem_irm=resp_tem_irm,
                                                   resp_quantos=resp_quantos, resp_tem_anim=resp_tem_anim,
                                                   resp_qual=resp_qual, resp_pais_sep=resp_pais_sep,
                                                   resp_qto_tempo=resp_qto_tempo, ra=ra)
            db.session.add(anam_responsavel)
            db.session.commit()
            return redirect(url_for('anam_rel_familiar', ra=ra))
        return render_template('Anamnese/anam_responsavel.html', detalhe_aluno=aluno_cadastro)

    # ROTA PARA A PAGINA RELACIONAMENTO FAMILIAR

    @app.route('/anam_rel_familiar/<int:ra>', methods=('GET', 'POST'))
    def anam_rel_familiar(ra):
        aluno_cadastro = get_aluno(Aluno, ra)
        if request.method == 'POST':
            rel_fam_momento = request.form['rel_fam_momento']
            rel_fam_ativ_mae = request.form['rel_fam_ativ_mae']
            rel_fam_ativ_pai = request.form['rel_fam_ativ_pai']
            rel_fam_rel_irmaos = request.form['rel_fam_rel_irmaos']
            rel_fam_cuidados_outros = request.form['rel_fam_cuidados_outros']
            anam_rel_familiar = AnamneseRelFamiliar(rel_fam_momento=rel_fam_momento, rel_fam_ativ_mae=rel_fam_ativ_mae,
                                                    rel_fam_ativ_pai=rel_fam_ativ_pai,
                                                    rel_fam_rel_irmaos=rel_fam_rel_irmaos,
                                                    rel_fam_cuidados_outros=rel_fam_cuidados_outros, ra=ra)
            db.session.add(anam_rel_familiar)
            db.session.commit()
            return redirect(url_for('anam_primeiros_anos', ra=ra))
        return render_template('Anamnese/anam_rel_familiar.html', detalhe_aluno=aluno_cadastro)

    # ROTA PARA A PAGINA PRIMEIROS ANOS
    @app.route('/anam_primeiros_anos/<int:ra>', methods=('GET', 'POST'))
    def anam_primeiros_anos(ra):
        aluno_cadastro = get_aluno(Aluno, ra)
        if request.method == 'POST':
            prim_anos_condicoes = request.form['prim_anos_condicoes']
            prim_anos_espacos = request.form['prim_anos_espacos']
            anam_primeiros_anos = AnamnesePrimeirosAnos(prim_anos_condicoes=prim_anos_condicoes,
                                                        prim_anos_espacos=prim_anos_espacos, ra=ra)
            db.session.add(anam_primeiros_anos)
            db.session.commit()
            return redirect(url_for('anam_dia_dia', ra=ra))
        return render_template('Anamnese/anam_prim_anos.html', detalhe_aluno=aluno_cadastro)

    # ROTA PARA A PAGINA DIA A DIA
    @app.route('/anam_dia_dia/<int:ra>', methods=('GET', 'POST'))
    def anam_dia_dia(ra):
        aluno_cadastro = get_aluno(Aluno, ra)
        if request.method == 'POST':
            dia_dia_horas_dormir = request.form['dia_dia_horas_dormir']
            dia_dia_horas_acordar = request.form['dia_dia_horas_acordar']
            dia_dia_faz_ativ = request.form['dia_dia_faz_ativ']
            dia_dia_quais = request.form['dia_dia_quais']
            dia_dia_qtas_vezes = request.form['dia_dia_qtas_vezes']
            dia_dia_brinca_so = request.form['dia_dia_brinca_so']
            dia_dia_com_quem = request.form['dia_dia_com_quem']
            dia_dia_cont_elet = request.form['dia_dia_cont_elet']
            dia_dia_elet_quais = request.form['dia_dia_elet_quais']
            dia_dia_org_brinq = request.form['dia_dia_org_brinq']
            dia_dia_hab_leitura = request.form['dia_dia_hab_leitura']
            dia_dia_ouvir_mus = request.form['dia_dia_ouvir_mus']
            dia_dia_tipo_mus = request.form['dia_dia_tipo_mus']
            dia_dia_rotina = request.form['dia_dia_rotina']
            anam_dia_dia = AnamneseDiaDia(dia_dia_horas_dormir=dia_dia_horas_dormir,
                                          dia_dia_horas_acordar=dia_dia_horas_acordar,
                                          dia_dia_faz_ativ=dia_dia_faz_ativ, dia_dia_quais=dia_dia_quais,
                                          dia_dia_qtas_vezes=dia_dia_qtas_vezes, dia_dia_brinca_so=dia_dia_brinca_so,
                                          dia_dia_com_quem=dia_dia_com_quem, dia_dia_cont_elet=dia_dia_cont_elet,
                                          dia_dia_elet_quais=dia_dia_elet_quais, dia_dia_org_brinq=dia_dia_org_brinq,
                                          dia_dia_hab_leitura=dia_dia_hab_leitura, dia_dia_ouvir_mus=dia_dia_ouvir_mus,
                                          dia_dia_tipo_mus=dia_dia_tipo_mus, dia_dia_rotina=dia_dia_rotina, ra=ra)
            db.session.add(anam_dia_dia)
            db.session.commit()
            return redirect(url_for('anam_vida_social', ra=ra))
        return render_template('Anamnese/anam_dia_dia.html', detalhe_aluno=aluno_cadastro)

    # ROTA PARA A PAGINA VIDA SOCIAL
    @app.route('/anam_vida_social/<int:ra>', methods=('GET', 'POST'))
    def anam_vida_social(ra):
        aluno_cadastro = get_aluno(Aluno, ra)
        if request.method == 'POST':
            vs_lazer = request.form['vs_lazer']
            vs_iter_loc_publico = request.form['vs_iter_loc_publico']
            vs_iter_casa = request.form['vs_iter_casa']
            anam_vida_social = AnamneseVidaSocial(vs_lazer=vs_lazer, vs_iter_loc_publico=vs_iter_loc_publico,
                                                  vs_iter_casa=vs_iter_casa, ra=ra)
            db.session.add(anam_vida_social)
            db.session.commit()
            return redirect(url_for('anam_viv_pessoal', ra=ra))
        return render_template('Anamnese/anam_vida_social.html', detalhe_aluno=aluno_cadastro)

    # ROTA PARA A PAGINA VIVÊNCIA PESSOAL
    @app.route('/anam_viv_pessoal/<int:ra>', methods=('GET', 'POST'))
    def anam_viv_pessoal(ra):
        aluno_cadastro = get_aluno(Aluno, ra)
        if request.method == 'POST':
            vp_medos = request.form['vp_medos']
            vp_quais_medos = request.form['vp_quais_medos']
            vp_quais_atit = request.form['vp_quais_atit']
            vp_trauma = request.form['vp_trauma']
            vp_trauma_quais = request.form['vp_trauma_quais']
            anam_viv_pessoal = AnamneseVivPessoal(vp_medos=vp_medos, vp_quais_medos=vp_quais_medos,
                                                  vp_quais_atit=vp_quais_atit, vp_trauma=vp_trauma,
                                                  vp_trauma_quais=vp_trauma_quais, ra=ra)
            db.session.add(anam_viv_pessoal)
            db.session.commit()
            return redirect(url_for('anam_alimentacao', ra=ra))
        return render_template('Anamnese/anam_viv_pessoais.html', detalhe_aluno=aluno_cadastro)

    # ROTA PARA A PAGINA ALIMENTAÇÃO
    @app.route('/anam_alimentacao/<int:ra>', methods=('GET', 'POST'))
    def anam_alimentacao(ra):
        aluno_cadastro = get_aluno(Aluno, ra)
        if request.method == 'POST':
            al_amamentou = request.form['al_amamentou']
            al_restricao = request.form['al_restricao']
            al_quais = request.form['al_quais']
            anam_alimentacao = AnamneseAlimentacao(al_amamentou=al_amamentou, al_restricao=al_restricao,
                                                   al_quais=al_quais, ra=ra)
            db.session.add(anam_alimentacao)
            db.session.commit()
            return redirect(url_for('anam_sono', ra=ra))
        return render_template('Anamnese/anam_alimentacao.html', detalhe_aluno=aluno_cadastro)

    # ROTA PARA A PAGINA SONO
    @app.route('/anam_sono/<int:ra>', methods=('GET', 'POST'))
    def anam_sono(ra):
        aluno_cadastro = get_aluno(Aluno, ra)
        if request.method == 'POST':
            sono_divide_quarto = request.form['sono_divide_quarto']
            sono_divide_com_quem = request.form['sono_divide_com_quem']
            sono_dorme_dia = request.form['sono_dorme_dia']
            sono_tem_rotina = request.form['sono_tem_rotina']
            sono_qual_rotina = request.form['sono_qual_rotina']
            sono_como_e = request.form['sono_como_e']
            anam_sono = AnamneseSono(sono_divide_quarto=sono_divide_quarto, sono_divide_com_quem=sono_divide_com_quem,
                                     sono_dorme_dia=sono_dorme_dia, sono_tem_rotina=sono_tem_rotina,
                                     sono_qual_rotina=sono_qual_rotina, sono_como_e=sono_como_e, ra=ra)
            db.session.add(anam_sono)
            db.session.commit()
            return redirect(url_for('anam_saude', ra=ra))
        return render_template('Anamnese/anam_sono.html', detalhe_aluno=aluno_cadastro)

    # ROTA PARA A PAGINA SAÚDE
    @app.route('/anam_saude/<int:ra>', methods=('GET', 'POST'))
    def anam_saude(ra):
        aluno_cadastro = get_aluno(Aluno, ra)
        if request.method == 'POST':
            saude_tem_questao = request.form['saude_tem_questao']
            saude_relate = request.form['saude_relate']
            saude_cirurgia = request.form['saude_cirurgia']
            saude_ciruria_qual = request.form['saude_ciruria_qual']
            saude_acidente = request.form['saude_acidente']
            saude_acidente_como_foi = request.form['saude_acidente_como_foi']
            saude_doencas_inf = request.form['saude_doencas_inf']
            saude_alergia = request.form['saude_alergia']
            saude_alergia_qual = request.form['saude_alergia_qual']
            saude_alergia_proc = request.form['saude_alergia_proc']
            saude_alergia_fam = request.form['saude_alergia_fam']
            saude_alergia_fam_qual = request.form['saude_alergia_fam_qual']
            saude_convulsao = request.form['saude_convulsao']
            saude_convulsao_sit = request.form['saude_convulsao_sit']
            saude_otite = request.form['saude_otite']
            saude_otite_freq = request.form['saude_otite_freq']
            saude_audiom = request.form['saude_audiom']
            saude_audiom_qdo = request.form['saude_audiom_qdo']
            saude_audiom_alter = request.form['saude_audiom_alter']
            saude_exam_oft = request.form['saude_exam_oft']
            saude_exam_oft_qdo = request.form['saude_exam_oft_qdo']
            saude_exam_oft_alt = request.form['saude_exam_oft_alt']
            saude_exam_oft_grav = request.form['saude_exam_oft_grav']
            anam_saude = AnamneseSaude(saude_tem_questao=saude_tem_questao, saude_relate=saude_relate,
                                       saude_cirurgia=saude_cirurgia, saude_ciruria_qual=saude_ciruria_qual,
                                       saude_acidente=saude_acidente, saude_acidente_como_foi=saude_acidente_como_foi,
                                       saude_doencas_inf=saude_doencas_inf, saude_alergia=saude_alergia,
                                       saude_alergia_qual=saude_alergia_qual, saude_alergia_proc=saude_alergia_proc,
                                       saude_alergia_fam=saude_alergia_fam,
                                       saude_alergia_fam_qual=saude_alergia_fam_qual, saude_convulsao=saude_convulsao,
                                       saude_convulsao_sit=saude_convulsao_sit, saude_otite=saude_otite,
                                       saude_otite_freq=saude_otite_freq, saude_audiom=saude_audiom,
                                       saude_audiom_qdo=saude_audiom_qdo, saude_audiom_alter=saude_audiom_alter,
                                       saude_exam_oft=saude_exam_oft, saude_exam_oft_qdo=saude_exam_oft_qdo,
                                       saude_exam_oft_alt=saude_exam_oft_alt, saude_exam_oft_grav=saude_exam_oft_grav,
                                       ra=ra)
            db.session.add(anam_saude)
            db.session.commit()
            return redirect(url_for('anam_des_psicomotor', ra=ra))
        return render_template('Anamnese/anam_saude.html', detalhe_aluno=aluno_cadastro)

    # ROTA PARA A PAGINA DESENVOLVIMENTO PSICOMOTOR
    @app.route('/anam_des_psicomotor/<int:ra>', methods=('GET', 'POST'))
    def anam_des_psicomotor(ra):
        aluno_cadastro = get_aluno(Aluno, ra)
        if request.method == 'POST':
            psi_gestacao = request.form['psi_gestacao']
            psi_engatinhou = request.form['psi_engatinhou']
            psi_qdo_engatinhou = request.form['psi_qdo_engatinhou']
            psi_como_e = request.form['psi_como_e']
            psi_aspectos = request.form['psi_aspectos']
            psi_atend_fora_escola = request.form['psi_atend_fora_escola']
            psi_atend_fora_escola_qual = request.form['psi_atend_fora_escola_qual']
            anam_des_psicomotor = AnamneseDesPsicomotor(psi_gestacao=psi_gestacao, psi_engatinhou=psi_engatinhou,
                                                        psi_qdo_engatinhou=psi_qdo_engatinhou, psi_como_e=psi_como_e,
                                                        psi_aspectos=psi_aspectos,
                                                        psi_atend_fora_escola=psi_atend_fora_escola,
                                                        psi_atend_fora_escola_qual=psi_atend_fora_escola_qual, ra=ra)
            db.session.add(anam_des_psicomotor)
            db.session.commit()
            return redirect(url_for('anam_reac_emocionais', ra=ra))
        return render_template('Anamnese/anam_des_psicomotor.html', detalhe_aluno=aluno_cadastro)

    # ROTA PARA A PAGINA REAÇÕES EMOCIONAIS
    @app.route('/anam_reac_emocionais/<int:ra>', methods=('GET', 'POST'))
    def anam_reac_emocionais(ra):
        aluno_cadastro = get_aluno(Aluno, ra)
        if request.method == 'POST':
            rea_emo_carac_marc = request.form['rea_emo_carac_marc']
            rea_emo_obj_efet = request.form['rea_emo_obj_efet']
            rea_emo_obj_efet_sit = request.form['rea_emo_obj_efet_sit']
            rea_emo_rel_pai = request.form['rea_emo_rel_pai']
            rea_emo_rel_mae = request.form['rea_emo_rel_mae']
            rea_emo_rel_avos = request.form['rea_emo_rel_avos']
            rea_emo_rel_cuid = request.form['rea_emo_rel_cuid']
            anam_reac_emocionais = AnamneseReacEmocionais(rea_emo_carac_marc=rea_emo_carac_marc,
                                                          rea_emo_obj_efet=rea_emo_obj_efet,
                                                          rea_emo_obj_efet_sit=rea_emo_obj_efet_sit,
                                                          rea_emo_rel_pai=rea_emo_rel_pai,
                                                          rea_emo_rel_mae=rea_emo_rel_mae,
                                                          rea_emo_rel_avos=rea_emo_rel_avos,
                                                          rea_emo_rel_cuid=rea_emo_rel_cuid, ra=ra)
            db.session.add(anam_reac_emocionais)
            db.session.commit()
            return redirect(url_for('anam_obs_finais', ra=ra))
        return render_template('Anamnese/anam_reac_emocionais.html', detalhe_aluno=aluno_cadastro)

    # ROTA PARA A PAGINA OBSERVAÇÕES FINAIS
    @app.route('/anam_obs_finais/<int:ra>', methods=('GET', 'POST'))
    def anam_obs_finais(ra):
        aluno_cadastro = get_aluno(Aluno, ra)
        if request.method == 'POST':
            obs_finais = request.form['obs_finais']
            anam_obs_finais = AnamneseObsFinais(obs_finais=obs_finais, ra=ra)
            db.session.add(anam_obs_finais)
            db.session.commit()
            return redirect(url_for('consulta_anamnese', ra=ra))
        return render_template('Anamnese/anam_obs_finais.html', detalhe_aluno=aluno_cadastro)

    # ROTA PARA A PAGINA CONSULTAR ANAMNESE
    @app.route('/consulta_anamnese/<int:ra>')
    def consulta_anamnese(ra):
        aluno_cadastro = get_aluno(Aluno, ra)
        return render_template('Anamnese/consulta_anamnese.html', detalhe_aluno=aluno_cadastro)
