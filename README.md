# myhost

###Dar permissao ao hosts

Exemplo<br>
sudo chown bmarcondes:bmarcondes /etc/hosts

--------------------------

###Criar alias para atalho

Exemplo<br>
alias myhost="python ~/git/myhost/main.py"

--------------------------

###Cria o host default
Limpar todo o arquivo de hosts antes de executar esse comando

Exemplo<br>
myhost init

--------------------------
###Trocar o host
Criar um arquivo dentro da pasta hosts
Nesse exemplo existe um arquivo chamado teste.host

Exemplo<br>
myhost teste

--------------------------

###Zerar o host
Nao colocar nome de arquivo

Exemplo<br>
myhost

--------------------------

###Ler o host atual

Exemplo<br>
myhost read
