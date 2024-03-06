
from dmtoolbox import nginx_controller as nc

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

# ============= #
#  Observações  #
# ============= #

# Ao rodar esse código lembre-se de ter configurado todo o ambiente e com arquivos corretos para receber as configurações

# Se rodar no linux ele irá editar o default.conf contino no sites-available, então cuidado!!



# O setup já inclui configuração e start, então basta 1 comando para ter tudo configurado e rodando
# Mas atenção ao que for passado nas diretivas e no content, caso não esteja condizente com o padrão do nginx
# certamente irá indicar um erro
nc.setup_nginx(directives=directives, config_content=config_content)


if nc.is_nginx_running():
    print("NGINX está rodando.")
else:
    print("NGINX não está rodando.")
    
    
nc.stop_nginx()
