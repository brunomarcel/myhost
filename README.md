# myhost

###Dar permissao ao hosts

Exemplo
sudo chown bmarcondes:bmarcondes /etc/hosts

--------------------------

###Criar alias para atalho

Exemplo
alias myhost="python ~/git/myhost/main.py"

--------------------------

###Cria o host default
###Limpar todo o arquivo de hosts antes de executar esse comando

Exemplo
myhost init

--------------------------
###Trocar o host
###Criar um arquivo dentro da pasta hosts
###Nesse exemplo existe um arquivo chamado teste.host

Exemplo
myhost teste

--------------------------

###Zerar o host
###Nao colocar nome de arquivo

Exemplo
myhost

--------------------------

###Ler o host atual

Exemplo
myhost read
