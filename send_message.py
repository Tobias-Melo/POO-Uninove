from abc import ABC, abstractmethod

class Canal(ABC):
    def __init__(self, destinatario):
        self.destinatario = destinatario

    @abstractmethod
    def enviar_mensagem(self, mensagem):
        pass

class CanalTelefone(Canal):
    def __init__(self, telefone):
        super().__init__(telefone)

    def enviar_mensagem(self, mensagem):
        print(f"Enviando mensagem para {self.destinatario} via telefone: {mensagem}")

class CanalUsuario(Canal):
    def __init__(self, usuario):
        super().__init__(usuario)

    def enviar_mensagem(self, mensagem):
        print(f"Enviando mensagem para {self.destinatario} via usuário: {mensagem}")

class Mensagem(ABC):
    def __init__(self, conteudo):
        self.conteudo = conteudo

    @abstractmethod
    def enviar(self, canal):
        pass

class MensagemTexto(Mensagem):
    def __init__(self, conteudo, data_envio):
        super().__init__(conteudo)
        self.data_envio = data_envio

    def enviar(self, canal):
        mensagem = f"Texto: {self.conteudo}, Enviado em: {self.data_envio}"
        canal.enviar_mensagem(mensagem)

class MensagemVideo(Mensagem):
    def __init__(self, conteudo, formato, duracao):
        super().__init__(conteudo)
        self.formato = formato
        self.duracao = duracao

    def enviar(self, canal):
        mensagem = f"Vídeo: {self.conteudo}, Formato: {self.formato}, Duração: {self.duracao}"
        canal.enviar_mensagem(mensagem)

class MensagemFoto(Mensagem):
    def __init__(self, conteudo, formato):
        super().__init__(conteudo)
        self.formato = formato

    def enviar(self, canal):
        mensagem = f"Foto: {self.conteudo}, Formato: {self.formato}"
        canal.enviar_mensagem(mensagem)

class MensagemArquivo(Mensagem):
    def __init__(self, conteudo, formato):
        super().__init__(conteudo)
        self.formato = formato

    def enviar(self, canal):
        mensagem = f"Arquivo: {self.conteudo}, Formato: {self.formato}"
        canal.enviar_mensagem(mensagem)

def escolher_canal():
    print("Escolha o canal:")
    print("1 - WhatsApp")
    print("2 - Telegram")
    print("3 - Facebook")
    print("4 - Instagram")

    opcao_canal = input("Digite o número do canal desejado: ")
    
    if opcao_canal == "1":
        return CanalTelefone(input("Digite o número de telefone: "))
    elif opcao_canal == "2":
        opcao_usuario_telefone = input("Escolha 'usuario' ou 'telefone': ")
        if opcao_usuario_telefone.lower() == "usuario":
            return CanalUsuario(input("Digite o nome de usuário do Telegram: "))
        elif opcao_usuario_telefone.lower() == "telefone":
            return CanalTelefone(input("Digite o número de telefone do Telegram: "))
        else:
            print("Opção inválida.")
            return None
    elif opcao_canal == "3":
        return CanalUsuario(input("Digite o nome de usuário do Facebook: "))
    elif opcao_canal == "4":
        return CanalUsuario(input("Digite o nome de usuário do Instagram: "))
    else:
        print("Canal inválido.")
        return None

def escolher_mensagem():
    tipo_mensagem = input("Escolha o tipo de mensagem (texto/video/foto/arquivo): ")
    conteudo = input("Digite o conteúdo da mensagem: ")

    if tipo_mensagem.lower() == "texto":
        data_envio = input("Digite a data de envio da mensagem: ")
        return MensagemTexto(conteudo, data_envio)
    elif tipo_mensagem.lower() == "video":
        formato = input("Digite o formato do vídeo: ")
        duracao = input("Digite a duração do vídeo: ")
        return MensagemVideo(conteudo, formato, duracao)
    elif tipo_mensagem.lower() == "foto":
        formato = input("Digite o formato da foto: ")
        return MensagemFoto(conteudo, formato)
    elif tipo_mensagem.lower() == "arquivo":
        formato = input("Digite o formato do arquivo: ")
        return MensagemArquivo(conteudo, formato)
    else:
        print("Tipo de mensagem inválido. Escolha entre 'texto', 'video', 'foto' e 'arquivo'.")
        return None

# Interação com o usuário
canal = escolher_canal()
if canal:
    mensagem = escolher_mensagem()
    if mensagem:
        mensagem.enviar(canal)
