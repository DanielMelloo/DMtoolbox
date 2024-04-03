# DMToolBox v0.1.28.1 Release Notes

### Data de Lançamento
- 3 de Abril de 2024

### Destaques
- Isolamento do módulo `nginxUtils` devido a um bug na resolução de caminhos.

### Novos Recursos
- Nenhum novo recurso adicionado nesta versão.

### Melhorias
- Nenhuma melhoria implementada nesta versão.

### Correções de Bugs
- Isolamento do módulo `nginxUtils` devido a um bug na resolução de caminhos. O módulo será desativado nesta versão até que o bug seja corrigido.

### Problemas Conhecidos
- Nenhum problema adicional conhecido nesta versão.

### Instruções de Atualização
- Utilize o comando `pip install dmtoolbox --upgrade` para atualizar para a última versão.

### Agradecimentos
- Agradecemos à comunidade do GitHub por seu apoio contínuo.

### Mais Informações
Para mais informações sobre o DMToolBox, consulte a documentação atualizada no diretório [`Exemplos de Código`](https://github.com/DanielMelloo/dmtoolbox/tree/main/Exemplos%20de%20Código).

Para relatar problemas ou fornecer feedback, abra uma [issue no GitHub](https://github.com/DanielMelloo/dmtoolbox/issues). Seu feedback é fundamental para melhorarmos o DMToolBox.


# DMToolBox v0.1.28 Release Notes

### Data de Lançamento
- 03 de Abril de 2024

### Destaques
- Adição da função `plot_2d_function_tlwa` para plotagem de funções 2D.
- Mudança do nome do módulo `func` para `fmfunc` para maior clareza e consistência.
- Correção de dependências, isolando módulos nativos do Windows no add-on `dmtoolbox-win`, melhorando a compatibilidade do pacote `dmtoolbox`.

### Novos Recursos
- Adicionada a função `plot_2d_function_tlwa` para plotagem de funções 2D.
- Renomeado o módulo `func` para `fmfunc` para maior clareza e consistência.

### Melhorias
- Melhorada a compatibilidade do pacote `dmtoolbox` ao isolar módulos nativos do Windows no add-on `dmtoolbox-win`.

### Correções de Bugs
- Nenhuma correção de bug neste lançamento.

### Problemas Conhecidos
- Nenhum problema conhecido neste lançamento.

### Instruções de Atualização
- Utilize o comando `pip install dmtoolbox --upgrade` para atualizar para a última versão.

### Agradecimentos
- Agradecemos à comunidade do GitHub por seus valiosos comentários e sugestões que contribuíram para essas melhorias.

### Mais Informações
Para obter informações detalhadas sobre a utilização dos módulos atualizados, consulte a documentação atualizada no diretório [`Exemplos de Código`](https://github.com/DanielMelloo/dmtoolbox/tree/main/Exemplos%20de%20Código).

Para suporte adicional ou relatar problemas, por favor, abra uma [issue no GitHub](https://github.com/DanielMelloo/dmtoolbox/issues). Estamos sempre abertos ao seu feedback para continuarmos melhorando o DMToolBox.

# DMToolBox v0.1.27 Release Notes

### Data de Lançamento
- 15 de Março de 2024

### Destaques
- Otimização significativa do desempenho em diversos módulos.
- Aprimoramento da documentação em toda a biblioteca.

### Novos Recursos
- Nenhum novo recurso adicionado nesta versão.

### Melhorias
- Significativa otimização de desempenho em vários módulos, resultando em execuções mais rápidas.
- Melhorias adicionais na documentação para tornar o uso dos módulos mais claro e intuitivo.

### Correções de Bugs
- Nenhuma correção de bug neste lançamento.

### Problemas Conhecidos
- A função `setup_available_port` do módulo `portTools` ainda está com problemas para identificar a porta disponível devido a incompatibilidades na verificação com o servidor web e o servidor local.

### Instruções de Atualização
- Utilize o comando `pip install dmtoolbox --upgrade` para atualizar para a última versão.

### Agradecimentos
- Agradecemos à comunidade do GitHub por seus valiosos comentários e sugestões que ajudaram a tornar o DMToolBox ainda melhor.

### Mais Informações
Para obter informações detalhadas sobre a utilização dos módulos atualizados, consulte a documentação atualizada no diretório [`Exemplos de Código`](https://github.com/DanielMelloo/dmtoolbox/tree/main/Exemplos%20de%20Código).

Para suporte adicional ou relatar problemas, por favor, abra uma [issue no GitHub](https://github.com/DanielMelloo/dmtoolbox/issues). Estamos sempre abertos ao seu feedback para continuarmos melhorando o DMToolBox.


# DMToolBox v0.1.26 Release Notes

### Data de Lançamento
- 05 de Março de 2024

### Destaques
- Introdução do módulo de controle NGINX para Windows e Linux.

### Novos Recursos
- Controladores NGINX específicos para Windows e Linux com funcionalidade automática de detecção de SO.
- Funções de início e parada do NGINX diretamente do Python.

### Melhorias
- Melhoria na performance do módulo de importação de dados.
- Interface de linha de comando aprimorada para o módulo de estatísticas.
- Generalização de criação de configurações.
- Generalização maior de sistemas operacionais.
- Generalização de criação de diretivas via dicionário.
- Integração de modificação de arquivos distintos por passagem de argumentos.

### Correções de Bugs
- Correção de comandos do NGINX no linux por generalização via polimorfismo de classe.

### Problemas Conhecidos
- O módulo de visualização de dados ainda não é compatível com o macOS.

### Instruções de Atualização
- Utilize o comando `pip install dmtoolbox --upgrade` para atualizar para a última versão.

### Agradecimentos
- Obrigado à comunidade do GitHub que contribuiu com pull requests e reportou bugs.

### Mais Informações
Para mais informações sobre a utilização dos novos recursos, consulte a documentação atualizada no diretório [`Exemplos de Código`](https://github.com/DanielMelloo/dmtoolbox/tree/main/Exemplos%20de%20Código)
---

Para suporte, entre em contato através de [issues no GitHub](https://github.com/DanielMelloo/dmtoolbox/issues). Agradecemos o feedback para continuarmos melhorando o DMToolBox.
