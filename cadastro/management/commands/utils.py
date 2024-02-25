import random
from django.core.management.base import BaseCommand
from faker import Faker
from cadastro.models import Pessoa, Lideranca

class Command(BaseCommand):
    help = 'Populate fake data for testing purposes'

    def handle(self, *args, **kwargs):
        fake = Faker('pt_BR')
        liderancas = Lideranca.objects.all()

        bairros_sao_goncalo = [
            'Alcântara', 'Almerinda', 'Amendoeira', 'Anaia Grande', 'Anaia Pequeno', 'Antonina', 'Arsenal', 'Arrastão', 'Barro Vermelho', 'Barracão', 'Boa Vista', 'Boaçu', 'Bom Retiro', 'Brasilândia', 'Camarão', 'Centro (Rodo de S.G.)', 'Colubandê', 'Convanca', 'Cruzeiro do Sul', 'Eliane', 'Engenho do Roçado', 'Engenho Pequeno', 'Estrela do Norte', 'Fazenda dos Mineiros', 'Galo Branco', 'Gebara', 'Gradim', 'Guarani', 'Guaxindiba', 'Ieda', 'Ipiíba', 'Itaoca', 'Itaúna', 'Jardim Amendoeira', 'Jardim Catarina', 'Jardim Nova República', 'Joquei', 'Lagoinha', 'Laranjal', 'Lindo Parque', 'Luiz Caçador', 'Marambaia', 'Maria Paula', 'Mangueira', 'Miriambi', 'Monjolo', 'Morro do Castro', 'Mutondo', 'Mutuaguaçu', 'Mutuapira', 'Neves', 'Nova Cidade', 'Novo México', 'Pacheco', 'Palmeira', 'Paraíso', 'Parada 40', 'Patronato', 'Pita', 'Porto da Madama', 'Porto da Pedra', 'Porto do Rosa', 'Porto Novo', 'Porto Velho', 'Recanto das Acácias', 'Raul Veiga', 'Rio do Ouro', 'Rocha', 'Rosane', 'Sacramento', 'Salgueiro', 'Santa Catarina', 'Santa Isabel', 'Santa Luzia', 'São Miguel', 'Tiradentes', 'Trindade', 'Tribobó', 'Venda da Cruz', 'Vila Candoza', 'Vila Lara', 'Vila Lage', 'Vila Três', 'Vista Alegre'
        ]

        for _ in range(1000):  # Altere o número conforme necessário
            lideranca = random.choice(liderancas)
            bairro = random.choice(bairros_sao_goncalo)
            pessoa = Pessoa(
                nome=fake.name(),
                rua=fake.street_name(),
                numero=str(fake.building_number()),
                complemento='casa',
                bairro=bairro,
                cidade='São Gonçalo',
                estado='RJ',
                cep=fake.postcode(),
                sexo=random.choice(['M', 'H']),
                idade=random.randint(18, 80),
                titulo_eleitor=fake.random_number(digits=10),
                zona_eleitoral=fake.random_number(digits=3),
                secao_eleitoral=fake.random_number(digits=3),
                nome_mae=fake.name_female(),
                lideranca=lideranca
            )
            pessoa.save()
            print(f"Nome: {pessoa.nome}, Cidade: {pessoa.cidade}")

        self.stdout.write(self.style.SUCCESS('Fake data populated successfully'))
