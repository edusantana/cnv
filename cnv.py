import click
import functools
from click_didyoumean import DYMGroup
import pdb
import json
import yaml

CONTEXT_SETTINGS = dict(
    help_option_names=['-h', '--help']
)


@click.group(context_settings=CONTEXT_SETTINGS)
@click.version_option()
def cli():
    """
    Comunicação Não Violenta (cnv)

    Script para auxiliar na utilização da comunicação não violenta.

    """
    pass

NECESSIDADES={"Conexão": ["aceitação", "afeição", "amor", "apoio", "apreciação", "carinho", "compaixão", "companheirismo", "compreender e ser compreendido", "comunicação", "comunidade", "confiança", "conhecer e ser conhecido", "consideração", "consistência", "cooperação", "criação-educação", "empatia", "estabilidade", "inclusão", "intimidade", "pertencimento", "proximidade", "reciprocidade", "respeito", "respeito próprio", "segurança", "segurança", "ver e ser visto"],
    "Significado": ["aprendizado", "auto-expressão", "celebração da vida", "clareza", "competência", "compreensão da matéria", "consciência", "consciência", "contribuição", "crescimento", "criatividade", "desafio", "descoberta", "eficiência", "entendimento", "esperança", "estímulo", "luto", "participação", "propósito", "ter significado"],
    "Autonomia":["escolha", "espaço", "espontaneidade", "liberdade", "independência"],
    "Honestidade": ["autenticidade", "integridade", "presença"],
    "Paz":["beleza", "comunhão", "harmonia", "igualdade", "inspiração", "ordem", "tranquilidade"],
    "Diversão": ["alegria", "humor"],
    "Bem-estar Físico": ["abrigo", "água", "ar", "comida", "descanso", "sono", "expressão sexual", "movimento", "exercício", "segurança", "toque"]
    }

@cli.command()
def necessidades():
    """
    Exibe a lista de necessidades.
    """

    click.echo(yaml.dump(NECESSIDADES, encoding='utf-8', allow_unicode=True))

SENTIMENTOS = {
    "MEDO": ["apreensivo", "assustado", "aterrorizado", "cauteloso", "desconfiado", "em pânico", "mal pressentimento", "medo", "pavor", "petrificado", "preocupado", "suspeito"],
    "IRRITADO": ["consternado", "desagradado", "descontente", "exasperado", "frustrado", "impaciente", "irritado"],
    "RAIVA": ["enfurecido", "furioso", "indignado", "irado", "ressentido"],
    "ENVERGONHADO": ["culpado", "envergonhado", "mortificado", "perturbado"],
    }

@cli.command()
def sentimentos():
    """
    Exibe a lista de sentimentos.
    """

    click.echo(yaml.dump(SENTIMENTOS, encoding='utf-8', allow_unicode=True))


@cli.command()
@click.option('-q','--quando','evento',metavar='<evento>', help='evento ocorrido. Ex: -e "você falou que iria me chegar cedo', required=True, prompt=True)
@click.option('-s','--senti', 'sentimento', metavar='<sentimento>', help='sentimento sentido durante o evento. ex: --senti "raiva"', required=True, prompt=True)
@click.option('-v','--valor', is_flag=True, help="Informa que necessidade será interpretada como um valor.")
@click.option('-n','--necessidade', 'necessidade', metavar='<necessidade|valor>', help='necessidade, ex: --necessidade "ordem"',  required=True, prompt=True)
def dizer(evento, sentimento, valor, necessidade):
    """
    Falar utilizando a CNV.
    """

    necessidade_ou_valor = "Valor" if valor else "Necessidade"

    frase = {
        "Quando": evento,
        "Sentimento": sentimento,
        necessidade_ou_valor: necessidade
    }

    quando = "Quando(%s) " % (evento)
    senti = "Senti(%s) " % (sentimento)
    

    click.echo(frase)
    click.echo(quando + senti)
