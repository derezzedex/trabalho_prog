from classes import *
from playhouse.shortcuts import model_to_dict
import os
import json

if os.path.exists(arquivo):
    os.remove(arquivo)

try:
    db.connect()
    db.create_tables([
        TipoItem,
        Item,
        Local,
        TipoEntidade,
        Entidade.inventario.get_through_model(),
        Entidade,
        Inimigo,
        Personagem,
        Quest.recompensa.get_through_model(),
        Quest,
        NPC.quests.get_through_model(),
        NPC,
        Jogo.mapa.get_through_model(),
        Jogo.personagens.get_through_model(),
        Jogo.npcs.get_through_model(),
        Jogo,
    ])
except OperationalError as erro:
    print("Erro:", erro)


# =================== TipoItem ===================
equipamento_espada = TipoItem.create(
    nome="Equipamento",
    subtipo="Espada"
)
consumivel_pocao = TipoItem.create(
    nome="Consumível",
    subtipo="Poção"
)
arma_cajado = TipoItem.create(
    nome="Arma",
    subtipo="Cajado"
)

# =================== Item ===================

lamina_doran = Item.create(
    nome="Lâmina de Doran",
    desc="Criado por Doran, um artesão brilhante.",
    tipo=equipamento_espada,
    ataque=8.0,
    defesa=80.0
)
pocao_corrupta = Item.create(
    nome="Poção corrupta",
    desc="Habilidades e ataques aplicam um efeito de queimadura no alvo.",
    tipo=consumivel_pocao,
    durabilidade=3.0,
    durabilidade_max=3.0
)
cajado_arcanjo = Item.create(
    nome="Cajado do Arcanjo",
    desc="Cajado divino.",
    tipo=arma_cajado,
    ataque=80.0,
)

# =================== Local ===================

ionia = Local.create(
    nome="Ionia",
    desc="Rodeada por águas traiçoeiras, Ionia é composta por várias províncias aliadas dispersas ao longo do arquipélago gigantesco conhecido como as Primeiras Terras."
)
freljord = Local.create(
    nome="Freljord",
    desc="É uma terra severa e implacável. Orgulhoso e ferozmente independente, seu povo é composto de guerreiros natos, com uma forte cultura de saqueamento."
)
ixtal = Local.create(
    nome="Ixtal",
    desc="Reconhecida por seu domínio da magia elemental, Ixtal foi uma das primeiras nações independentes que se uniram ao império shurimane."
)

# =================== TipoEntidade ===================

humano_atirador = TipoEntidade.create(
    raca="Humano",
    classe="Atirador"
)
vastaya_mago = TipoEntidade.create(
    raca="Vastaya",
    classe="Mago"
)
yordle_lutador = TipoEntidade.create(
    raca="Yordle",
    classe="Lutador"
)

# =================== Entidade ===================

ent_jhin = Entidade.create(
    tipo=humano_atirador,
    nivel=9.0,
    experiencia=220.5,
    vida=1211.4,
    defesa=101.2,
    ataque=205.0,
    origem=ionia
)
ent_jhin.inventario.add([lamina_doran])

ent_neeko = Entidade.create(
    tipo=vastaya_mago,
    nivel=5.0,
    experiencia=101.5,
    vida=1010.9,
    defesa=80.2,
    ataque=102.0,
    origem=ixtal
)
ent_neeko.inventario.add([cajado_arcanjo])

ent_gnar = Entidade.create(
    tipo=yordle_lutador,
    nivel=11.0,
    experiencia=240.5,
    vida=1527.7,
    defesa=210.2,
    ataque=291.8,
    origem=freljord
)
ent_gnar.inventario.add([pocao_corrupta])

# =================== Inimigo ===================

inim_neeko = Inimigo.create(
    nome="Neeko",
    entidade=ent_neeko
)

# =================== Personagem ===================

personagem_jhin = Personagem.create(
    nome="Jhin",
    nome_jogador="Richard",
    entidade=ent_jhin
)

# =================== Quest ===================

ajudar_freljord = Quest.create(
    nome="Freljord em apuros!",
    desc="Ajude Freljord a enfrentar os Observadores.",
    destino=freljord,
)
ajudar_freljord.recompensa.add([lamina_doran])

# =================== NPC ===================

npc_gnar = NPC.create(
    nome="Gnar",
    entidade=ent_gnar,
)
npc_gnar.quests.add([ajudar_freljord])

# =================== Jogo ===================

jogo = Jogo.create(
    nome_aventura="Lendas de Runeterra",
)

jogo.mapa.add([freljord, ixtal, ionia])
jogo.personagens.add([personagem_jhin])
jogo.npcs.add([npc_gnar])

jogo_dict = model_to_dict(jogo, manytomany=True, recurse=True)
print(json.dumps(jogo_dict))
