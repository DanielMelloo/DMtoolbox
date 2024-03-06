
# Documentação do Controlador NGINX

O módulo Controlador NGINX é uma biblioteca Python projetada para facilitar o gerenciamento do servidor web NGINX em ambientes Windows e Linux. Esta documentação oferece uma visão geral de como utilizar o módulo, incluindo exemplos de código para operações comuns, configurações avançadas e solução de problemas.



- [Documentação do Controlador NGINX](#documentação-do-controlador-nginx)
  - [Pré-requisitos](#pré-requisitos)
  - [Observações](#observações)
    - [Adendo para usuários do Windows](#adendo-para-usuários-do-windows)
    - [Adendo para usuários Linux](#adendo-para-usuários-linux)
  - [Instalação do Pacote DMToolBox](#instalação-do-pacote-dmtoolbox)
  - [Como Usar](#como-usar)
    - [Importando o controlador](#importando-o-controlador)
    - [Utilização Básica](#utilização-básica)
    - [Iniciando o NGINX](#iniciando-o-nginx)
    - [Parando o NGINX](#parando-o-nginx)
    - [Verificando o Estado do NGINX](#verificando-o-estado-do-nginx)
    - [Configurando o NGINX](#configurando-o-nginx)
    - [Reiniciando o NGINX](#reiniciando-o-nginx)
  - [Configurações Avançadas](#configurações-avançadas)
    - [Exemplo de Configuração Avançada](#exemplo-de-configuração-avançada)
  - [Solução de Problemas](#solução-de-problemas)
  - [Contribuições e Suporte](#contribuições-e-suporte)

## Pré-requisitos

- Python 3.x
- NGINX instalado no sistema

## Observações

### Adendo para usuários do Windows
Se você está no Windows, é necessário que a pasta do NGINX versão 1.24.0 esteja localizada em `C:\Users\<Seu Usuário>\AppData\LocalLow\`. Isso permite que o módulo controle o NGINX corretamente no ambiente Windows.

### Adendo para usuários Linux
No Linux, você deve especificar qual arquivo de configuração do NGINX deseja usar, caso não queira utilizar o arquivo `default.conf`. Isso é importante para garantir que as alterações sejam aplicadas corretamente ao arquivo desejado.
## Instalação do Pacote DMToolBox

O módulo faz parte do pacote DMToolBox, que pode ser instalado via pip. Execute o seguinte comando no seu terminal:

```bash
pip install dmtoolbox
```

## Como Usar

### Importando o controlador

Você pode importar o controlador NGINX diretamente do pacote [`dmtoolbox`](https://github.com/DanielMelloo/dmtoolbox/tree/main) usando um dos seguintes métodos:

```python
from dmtoolbox import nginx_controller
```

```python
from dmtoolbox.nginxUtils import nginx_controller
```

Alternativamente, se você tiver baixado o módulo [`nginxUtils.py`](https://github.com/DanielMelloo/dmtoolbox/blob/main/dmtoolbox/nginxUtils.py) separadamente:

```python
from nginxUtils import nginx_controller
```

### Utilização Básica

O módulo já inclui uma instância padrão do controlador NGINX adequada ao seu sistema operacional. No entanto, se desejar criar uma nova instância do controlador, você pode fazer isso da seguinte maneira:

**Para Windows:**

```python
from dmtoolbox import WindowsNginxController
nginx_controller = WindowsNginxController()
```

**Para Linux:**

```python
from dmtoolbox import LinuxNginxController
nginx_controller = LinuxNginxController()
```

### Iniciando o NGINX

Para iniciar o servidor NGINX:

```python
nginx_controller.start_nginx()
```

### Parando o NGINX

Para parar o servidor NGINX:

```python
nginx_controller.stop_nginx()
```

### Verificando o Estado do NGINX

Para verificar se o NGINX está em execução:

```python
if nginx_controller.is_nginx_running():
    print("NGINX está rodando.")
else:
    print("NGINX não está rodando.")
```

### Configurando o NGINX

Para configurar o servidor NGINX com diretivas personalizadas:

```python
directives = {
    'listen': '80',
    'server_name': 'meusite.com'
}

config_content = """
server {
    listen 80;
    server_name meusite.com;
    location / {
        proxy_pass http://127.0.0.1:5000;
    }
}
"""

nginx_controller.setup_nginx(directives=directives, config_content=config_content)
```

### Reiniciando o NGINX

Para reiniciar o servidor NGINX:

```python
nginx_controller.restart_nginx()
```

## Configurações Avançadas

O módulo permite personalizações avançadas da configuração do NGINX para atender a requisitos específicos, como balanceamento de carga, cache, entre outros. A [documentação oficial do NGINX](https://nginx.org/en/docs/) é um excelente recurso para explorar essas possibilidades.

### Exemplo de Configuração Avançada

Para configurar um balanceamento de carga simples:

```python
# Diretivas para verificar a consistência da configuração
directives = {
    'upstream myapp': lambda value: 'srv1.example.com' in value and 'srv2.example.com' in value,
    'listen': lambda value: value == '80',
    'proxy_pass': lambda value: value == 'http://myapp',
}

# Conteúdo da configuração para balanceamento de carga
config_content = """
upstream myapp {
    server srv1.example.com;
    server srv2.example.com;
}

server {
    listen 80;

    location / {
        proxy_pass http://myapp;
    }
}
"""

# Usando o método setup_nginx para configurar o NGINX com as diretivas e o conteúdo da configuração
nginx_controller.setup_nginx(directives=directives, config_content=config_content)
```

## Solução de Problemas

Caso encontre erros ou comportamentos inesperados ao usar o módulo, verifique a sintaxe das suas diretivas de configuração e assegure-se de que o NGINX está corretamente instalado no seu sistema. Para problemas mais complexos, consulte a documentação oficial do NGINX ou busque ajuda na comunidade.

## Contribuições e Suporte

Contribuições para o módulo são bem-vindas! Para reportar bugs, sugerir melhorias ou solicitar novas funcionalidades, sinta-se à vontade para abrir uma issue ou um pull request no repositório do projeto.

Para suporte adicional, entre em contato 

Esperamos que este guia facilite a integração do NGINX em seus projetos Python. Boa codificação!