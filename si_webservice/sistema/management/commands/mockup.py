# -*- coding: utf-8 -*-

from django.core.management.base import NoArgsCommand
from sistema.models import *
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from datetime import datetime, date

class Command(NoArgsCommand):
    def handle_noargs(self, **options):

        somemodel_ct = ContentType.objects.get(app_label='auth', model='user')

        grupoadmin = Group(name = 'admin')
        grupoadmin.save()
        grupoaluno = Group(name = 'aluno')
        grupoaluno.save()
        # grupocopiadora = Group(name = 'copiadora')
        # grupocopiadora.save()

        permadmin = Permission(name='Permissao admin', codename='permadmin',content_type=somemodel_ct)
        permadmin.save()
        permaluno = Permission(name='Permissao aluno', codename='permaluno',content_type=somemodel_ct)
        permaluno.save()

        # permcopiadora = Permission(name='Permissao copiadora', codename='permcopiadora',content_type=somemodel_ct)
        # permcopiadora.save()

        grupoadmin.permissions = [permadmin, permaluno]
        grupoaluno.permissions = [permaluno]
        # grupocopiadora.permissions = [permcopiadora]

        user = User.objects.create_user('admin', 'admin@admin.com', 'admin')
        user.is_superuser = True
        user.is_staff = True
        user.group = [grupoadmin]
        user.save()


        def criar_faculdade(faculdade1):
            faculdade=Faculdade()
            faculdade.nome=faculdade1
            faculdade.save()
            return faculdade

        def criar_participante(nome, sobrenome, faculdade, e_mail, telefone, curso, ano_ingresso):
            # user = User.objects.create_user(username=nome_sobrenome, email="aluno@aluno.com", password=nome_sobrenome)
            # user.is_staff = False
            # user.is_superuser = False
            # user.groups = [grupoaluno]
            # user.save()


            participante = Participante()
            participante.nome = nome
            participante.sobrenome=sobrenome
            participante.faculdade = faculdade
            participante.e_mail = e_mail
            participante.telefone = telefone
            participante.curso = curso
            participante.ano_ingresso = ano_ingresso
            participante.save()

            return participante


        def criar_atividade(nome, dia, horario, cap_participantes, pont_vendas, preco):
            atividade = Atividade()
            atividade.nome = nome
            atividade.dia = dia
            atividade.horario = horario
            atividade.cap_participantes = cap_participantes
            atividade.pont_vendas = pont_vendas
            atividade.preco = preco
            atividade.save()

            return atividade

        atividade1=criar_atividade("Marcos Pontes", 'Quarta-Feira', '11:00', '100', '5', '3')
        atividade2=criar_atividade("Wellington Nogueira", 'Terça-Feira', '11:00', '200', '5', '3')
        atividade3=criar_atividade("Guilherme Paulus Nogueira", 'Segunda-Feira', '11:00', '150', '5', '3')
        atividade4=criar_atividade("Sofia Esteves", 'Quinta-Feira', '11:00', '200', '5', '3')
        atividade5=criar_atividade("Sônia Hess", 'Sexta-Feira', '11:00', '200', '5', '3')

        def criar_ponto_venda(nome):
            ponto = PontodeVenda()
            ponto.nome = nome
            ponto.save()
            return ponto

        def criar_vendedor(nome):
            vendedor = Vendedor()
            vendedor.nome = nome
            vendedor.save()
            return vendedor


        faculdade1=criar_faculdade("Poli")
        faculdade2=criar_faculdade("FEA")
        faculdade3=criar_faculdade("ECA")
        faculdade4=criar_faculdade("FAU")
        faculdade5=criar_faculdade("IME")

        ponto_venda0=criar_ponto_venda("Nenhum")
        ponto_venda1=criar_ponto_venda("Bienio")
        ponto_venda2=criar_ponto_venda("Civil")
        ponto_venda3=criar_ponto_venda("Mecânica")
        ponto_venda4=criar_ponto_venda("Eletrica")
        ponto_venda5=criar_ponto_venda("FEA")

        vendedor1=criar_vendedor("PV")
        vendedor2=criar_vendedor("Marcos")
        vendedor3=criar_vendedor("Nicolas")
        vendedor4=criar_vendedor("Vinicius")

        participante1 = criar_participante("Pedro", "Nakachima", faculdade1, "pedro.nakachima@gmail.com", "989990992", "Engenharia Mecânica", "2014")
        participante2 = criar_participante("Marcos", "Thomas", faculdade2, "marcos.thomas@gmail.com", "989582514", "Engenharia Mecânica", "2014")
        participante3 = criar_participante("Vinicius", "Utsumi", faculdade3, "vinicius.utsumi@gmail.com", "978651565", "Engenharia Mecânica", "2014")
        participante4 = criar_participante("Nicolas", "Silva", faculdade4, "nicolas.silva@gmail.com", "923224528", "Engenharia Mecânica", "2014")


        # copiadora1 = criar_copiadora("Minerva", "minerva@minerva.com", faculdade1, "62.025.689/0001-66", "Minerva S/A", '(11) 999999999', "alguma rua", "www.exemplo.com", "EU")
        # copiadora2 = criar_copiadora("FEA Copy", "fea@fea.com", faculdade2, "62.025.666/0001-66", "FEA COPY LTDA", '(11) 777777777', "outra rua", "www.oi.com", "Outra pessoa")

        # maguilla = criar_aluno("rafael.maguilla", 'Masculino', faculdade1, '50.345.667-6', '412.884.958-89', copiadora1, 123, "Engenharia Eletrica", '(11) 99958-3868', '(11) 3835-8783', "Rua", "Complemento", '1994-09-29')
        # pv = criar_aluno("pedro.nakachima", 'Masculino', faculdade1, '78.385.667-X', '123.456.958-89', copiadora1, 43, "Engenharia Mecanica", '(11) 98999-0991', '(11) 3835-8783', "Rua", "Complemento", '1994-09-29')
        # vila = criar_aluno("rafael.vilarinho", 'Masculino', faculdade1, '12.345.334-X', '412.884.887-21', copiadora1, 22435, "Engenharia Civil", '(11) 99494-2535', '(11) 3835-8783', "Rua", "Complemento", '1994-09-29')
        # maria = criar_aluno("maria.carla", 'Feminino', faculdade1, '09.345.333-6', '123.884.333-12', copiadora1,  2325, "Engenharia Eletrica", '(11) 98492-6388', '(11) 3835-8783', "Rua", "Complemento", '1994-09-29')
        # lucas = criar_aluno("lucas.scarparo", 'Masculino', faculdade1, '01.301.612-6', '309.111.958-89', copiadora1, 1324, "Engenharia Mecanica", '(11) 98644-5073', '(11) 3835-8783', "Rua", "Complemento", '1994-09-29')


        # anunciante1 = criar_anunciante('Poli Jr', 'Junior Poli Estudos', '62.025.689/0001-66')
        # anunciante2 = criar_anunciante('Jacopiei', 'Jacopiei Servicos de Copias Ltda.', '20.451.891/0001-00')

        print 'Mockup feito com sucesso'
