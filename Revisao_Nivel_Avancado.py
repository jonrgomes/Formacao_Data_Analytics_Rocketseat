leituras = [
    {"sensor": "A1", "temp": 22.5},
    {"sensor": "A2", "temp": None},
    {"sensor": "A1", "temp": 23.1},
    {"sensor": "A3", "temp": 150.0}, # Anomalia
    {"sensor": "A2", "temp": 19.8},
]

class AnalisadorDeSensores:
    def __init__(self, dados_brutos):
        # O construtor recebe os dados originais e prepara uma lista vazia para os dados limpos
        self.dados = dados_brutos
        self.dados_limpos = []
        
    def limpar_dados(self):
        for leitura in self.dados:
            temperatura = leitura["temp"]
            
            # O Python permite verificar duas condições na mesma linha com o 'and'.
            # Usamos 'is not None' para evitar que o código quebre ao tentar comparar None com números.
            if temperatura is not None and temperatura <= 100.0:
                self.dados_limpos.append(leitura)

    def media_por_sensor(self):
        # Para calcular a média, precisamos de guardar duas informações por sensor: a soma das temperaturas e a contagem de leituras.
        somas = {}
        contagens = {}
        
        # 1. Agrupar as somas e as contagens usando os dados já limpos
        for leitura in self.dados_limpos:
            sensor = leitura["sensor"]
            temp = leitura["temp"]
            
            if sensor not in somas:
                somas[sensor] = 0
                contagens[sensor] = 0
                
            somas[sensor] += temp
            contagens[sensor] += 1
            
        # 2. Criar um novo dicionário apenas com o resultado final (a divisão)
        medias = {}
        for sensor in somas:
            medias[sensor] = somas[sensor] / contagens[sensor]
            
        return medias

# --- Execução do Código ---

# 1. Instanciamos a classe (criamos o objeto) passando a lista suja
analisador = AnalisadorDeSensores(leituras)

# 2. Pedimos ao objeto para limpar os seus próprios dados
analisador.limpar_dados()

# 3. Pedimos ao objeto para calcular as médias
resultado = analisador.media_por_sensor()

print("Média Final por Sensor:", resultado)