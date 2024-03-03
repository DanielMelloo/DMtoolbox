
![GitHub repo size](https://img.shields.io/github/repo-size/DanielMelloo/SpecMatch?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/DanielMelloo/SpecMatch?style=for-the-badge)
![Bitbucket open issues](https://img.shields.io/bitbucket/issues-raw/DanielMelloo/SpecMatch?style=for-the-badge)
![Bitbucket open pull requests](https://img.shields.io/bitbucket/pr-raw/DanielMelloo/SpecMatch?style=for-the-badge)


# DMutils


- [DMutils](#dmutils)
  - [Descrição](#descrição)
  - [Funcionalidades](#funcionalidades)
  - [Funcionalidades dos Módulos](#funcionalidades-dos-módulos)
    - [appdataGen.py](#appdatagenpy)
    - [createExeOnC.py](#createexeoncpy)
    - [exeGenerator.py](#exegeneratorpy)
    - [func.py](#funcpy)
    - [genJsons.py](#genjsonspy)
    - [nginxDefaults.py e nginxUtils.py](#nginxdefaultspy-e-nginxutilspy)
    - [numericFuncs.py](#numericfuncspy)
    - [osFuncs.py](#osfuncspy)
    - [portTools.py](#porttoolspy)
    - [regedit.py](#regeditpy)
  - [Instalação do Pacote DMutils](#instalação-do-pacote-dmutils)
    - [Pré-Requisitos](#pré-requisitos)
    - [Passo 1: Criação de um Ambiente Virtual (Opcional, mas Recomendado)](#passo-1-criação-de-um-ambiente-virtual-opcional-mas-recomendado)
    - [Passo 2: Instalação do Pacote DMutils](#passo-2-instalação-do-pacote-dmutils)
    - [Solução Alternativa: Instalação Manual das Dependências e Clonagem do Repositório](#solução-alternativa-instalação-manual-das-dependências-e-clonagem-do-repositório)
  - [Exemplos de Uso](#exemplos-de-uso)
  - [Contribuições](#contribuições)
  - [Autor](#autor)
  - [Licença](#licença)



## Descrição
Este pacote Python é uma coleção abrangente de ferramentas projetadas para facilitar a automação de tarefas e operações no ambiente Windows, manipulação avançada de arquivos e diretórios, criação e gestão de executáveis, manipulação de dados JSON, gerenciamento de configurações NGINX, análise numérica, e muito mais.


## Funcionalidades
- **Gerenciamento de Arquivos e Diretórios**: Criação e manipulação de estruturas de arquivos no AppData e outras localizações, com suporte para operações que requerem privilégios elevados.
- **Criação de Executáveis**: Utilitários para transformar scripts Python em executáveis independentes, facilitando a distribuição e execução.
- **Manipulação de JSON**: Ferramentas para converter dados para e de JSON, e atualizar scripts com novas declarações de variáveis baseadas em conteúdo JSON.
- **Gerenciamento do NGINX**: Funcionalidades para configurar, iniciar, parar e reiniciar o servidor NGINX, além de verificar e ajustar configurações de acordo com as necessidades do usuário.
- **Análise Numérica e Visualização**: Funções para manipulação matemática avançada, incluindo operações com matrizes, geração de tabelas formatadas, e plotagem de gráficos 2D e 3D.
- **Interação com o Sistema Operacional**: Utilitários para verificar privilégios de administrador, manipular registros do Windows, e mais.
- **Gerenciamento de Portas**: Ferramentas para verificar a disponibilidade de portas e configurar portas para aplicações.



## Funcionalidades dos Módulos
Cada módulo traz um conjunto de funcionalidades específicas, detalhadas a seguir:


### [appdataGen.py](https://danielmelloo.github.io/)
- Gerencia arquivos e diretórios no AppData LocalLow, permitindo a criação personalizada de estruturas de diretórios e arquivos de configuração.

### createExeOnC.py
- Facilita a criação de cópias da aplicação no disco local C, útil para a distribuição de software ou instalação local rápida.

### exeGenerator.py
- Utiliza o PyInstaller para converter scripts Python em executáveis autônomos, simplificando a distribuição de aplicações.

### func.py
- Oferece um conjunto diversificado de funções utilitárias para operações comuns, como manipulação de datas, tamanhos de arquivos, e caminhos de diretórios.

### genJsons.py
- Permite a conversão eficiente de dados para o formato JSON e vice-versa, além da atualização dinâmica de scripts com novos dados JSON.

### nginxDefaults.py e nginxUtils.py
- Proporcionam ferramentas para o gerenciamento detalhado de configurações do servidor NGINX, incluindo inicialização, parada, e verificação de status.

### numericFuncs.py
- Inclui funções para análises numéricas avançadas, manipulação de matrizes, e visualização de dados em 2D e 3D.

### osFuncs.py
- Contém utilitários para interações avançadas com o sistema operacional, como verificação de privilégios de administrador e manipulação de arquivos e diretórios.

### portTools.py
- Fornece métodos para verificar a disponibilidade de portas TCP/IP e selecionar portas disponíveis para aplicações.

### regedit.py
- Permite a criação e gerenciamento de entradas de registro do Windows, facilitando a integração com o sistema operacional.



## Instalação do Pacote DMutils

Para instalar o pacote DMutils de maneira eficiente e segura, siga os passos abaixo. Recomendamos a utilização de um ambiente virtual Python para evitar conflitos de dependências com outros pacotes instalados no sistema.

### Pré-Requisitos

- Certifique-se de que o Python está instalado em seu sistema. O DMutils é compatível com Python 3.6 ou superior.
- É recomendável ter o pip, o gerenciador de pacotes do Python, atualizado. Para atualizar o pip, execute o seguinte comando no terminal:
```bash
python -m pip install --upgrade pip
```

### Passo 1: Criação de um Ambiente Virtual (Opcional, mas Recomendado)

1. Abra um terminal.
2. Navegue até o diretório onde deseja armazenar o ambiente virtual e seu projeto.
3. Execute o comando para criar um ambiente virtual. Substitua `meuenv` pelo nome que deseja dar ao seu ambiente virtual:

python -m venv meuenv

4. Ative o ambiente virtual:

   - No Windows:
    ```powershell
    .\meuenv\Scripts\activate
    ```

    - No Unix ou MacOS:
    ```bash
    source meuenv/bin/activate
    ```

### Passo 2: Instalação do Pacote DMutils

Com o ambiente virtual ativado, instale o pacote DMutils utilizando o pip:
```bash
pip install DMutils
```

### Solução Alternativa: Instalação Manual das Dependências e Clonagem do Repositório

Caso encontre problemas ao instalar o pacote via pip, você pode optar por instalar manualmente as dependências e clonar o repositório do projeto. Primeiro, instale as dependências listadas no arquivo `requirements.txt`:
```bash
pip install -r requirements.txt
```

Em seguida, clone o repositório do GitHub ou baixe os arquivos do projeto diretamente para o seu ambiente de trabalho.




## Exemplos de Uso
Para cada módulo, exemplos detalhados de uso são fornecidos na documentação interna. Estes exemplos abrangem desde a criação de diretórios no AppData até a configuração avançada do NGINX e análise numérica com visualização de dados.

## Contribuições
Encorajamos contribuições! Se deseja sugerir melhorias, corrigir bugs ou adicionar novas funcionalidades, por favor, abra uma issue ou submeta um pull request.


## Autor

- Nome: Daniel Mello
- Website: [Portfólio](https://www.danielmello.tech)
- GitHub: [github.com/DanielMelloo](https://github.com/DanielMelloo)


## Licença
Este projeto é licenciado sob a GNU General Public License v3.0 - veja o arquivo [LICENSE](LICENSE) para mais detalhes.


[⬆ Voltar ao topo](#dmutils)