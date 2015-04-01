# myhost

###Dar permissao ao hosts
sudo chown <username>:<username> <path/to/hosts/file>

Exemplo
sudo chown bmarcondes:bmarcondes /etc/hosts

--------------------------

###Criar alias para atalho
alias myhost="python <path/to/arquivo/main.py>

Exemplo
alias myhost="python ~/git/myhost/main.py"

--------------------------

###Cria o host default
###Limpar todo o arquivo de hosts antes de executar esse comando

Exemplo
myhost init

--------------------------
###Trocar o host
myhost <filename>

Exemplo
myhost teste

--------------------------

###Zerar o host
Nao colocar nome de arquivo

Exemplo
myhost

--------------------------

###Ler o host atual

Exemplo
myhost read
