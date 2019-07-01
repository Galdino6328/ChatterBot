from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot


TiZ = ChatBot('Test')

convI = ['oi', 'olá', 'olá', 'bom dia', 'como vai?', 'estou bem']
convF = ['que filme você gosta?', 'eu gosto de Homem Aranha.', 'sério?', 'e você, qual filme gosta?']

TiZ.set_trainer(ListTrainer)

TiZ.train(convI)
TiZ.train(convF)

while True:
    quest = input('Você:')

    response = TiZ.get_response(quest)
    if float(response.confidence) > 0.5:
        print('TiZ:', response)
    else:
        print('TiZ: Não entendi, pode repetir eu aprendo com você!!!.')