# myhost

# Dar permissao ao hosts
sudo chown <username>:<username> <path/to/hosts/file>

# Exemplo
sudo chown bmarcondes:bmarcondes /etc/hosts

--------------------------

# Criar alias para atalho
alias myhost="python <path/to/arquivo/main.py>

# Exemplo
alias myhost="python ~/git/myhost/main.py"

--------------------------

# Trocar o host
# Nome do arquivo dentro da pasta "hosts" sem a extensao
myhost <filename>

# Exemplo
myhost tvuol

--------------------------

# Zerar o host
# Nao colocar nome de arquivo

# Exemplo
myhost

--------------------------

# Ler o host atual

# Exemplo
myhost read
