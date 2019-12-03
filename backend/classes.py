from peewee import *

arquivo = "rpg.db"
db = SqliteDatabase(arquivo)

class BaseModel(Model):
    class Meta():
        database = db

class TipoItem(BaseModel):
    nome = CharField()
    subtipo = CharField()

class Item(BaseModel):
    nome = CharField()
    desc = CharField()
    tipo = ForeignKeyField(TipoItem)
    # Estes atributos podem ou não existir em certo itens!
    durabilidade = IntegerField(null=True)
    durabilidade_max = IntegerField(null=True)
    ataque = FloatField(null=True)
    defesa = FloatField(null=True)

class Local(BaseModel):
    nome = CharField()
    desc = CharField()

class TipoEntidade(BaseModel):
    raca = CharField()
    classe = CharField()

class Entidade(BaseModel):
    tipo = ForeignKeyField(TipoEntidade)
    nivel = FloatField()
    experiencia = FloatField()
    vida = FloatField()
    ataque = FloatField()
    defesa = FloatField()
    origem = ForeignKeyField(Local)
    inventario = ManyToManyField(Item)

class Inimigo(BaseModel):
    nome = CharField()
    entidade = ForeignKeyField(Entidade)

class Personagem(BaseModel):
    nome = CharField()
    nome_jogador = CharField()
    entidade = ForeignKeyField(Entidade)

class Quest(BaseModel):
    nome = CharField()
    desc = CharField()
    destino = ForeignKeyField(Local)
    recompensa = ManyToManyField(Item)

class NPC(BaseModel):
    nome = CharField()
    entidade = ForeignKeyField(Entidade)
    quests = ManyToManyField(Quest)

class Jogo(BaseModel):
    nome_aventura = CharField()
    mapa = ManyToManyField(Local)
    personagens = ManyToManyField(Personagem)
    npcs = ManyToManyField(NPC)
