import datetime

class SystemInfo:
    def __init__(self):
        pass

    @staticmethod
    def obter_horario():
        now = datetime.datetime.now()
        resposta = 'São {} horas e {} minutos.'.format(now.hour, now.minute)
        return resposta