import sys, os

response = '\nmyhost init = Criar o host default\nmyhost clear = Limpa o hosts\nmyhost <filename> = Muda o host\n'
linha = []
curPath = os.path.dirname(os.path.realpath(__file__))

if len(sys.argv) > 1 and sys.argv[1] == "init":
	
	if os.path.isfile(curPath+'/default.host'):
		print "\nArquivo default.host ja existe\n"
		sys.exit()

	hosts = open('/etc/hosts', 'r')
	linhas = hosts.readlines()
	linhas.append("\n## MyHost\n")
	hosts.close()			

	default = open(curPath+'/default.host', 'w')
	default.writelines(linhas)
	default.close()

	print "\nCriado arquivo default.host\n"
else:

	if not os.path.isfile(curPath+'/default.host'):
		print "\nArquivo default.host nao existe"
		print "Execute myhost init\n"
		sys.exit()

	if len(sys.argv) > 1:

		default = open(curPath+'/default.host', 'r')
		linhas = default.readlines()
		default.close()

		if(sys.argv[1] == 'clear'):
			response = 'default'

		elif(sys.argv[1] == 'read'):

			response = sys.argv[1];

			hosts = open('/etc/hosts', 'r')
			linha = hosts.readlines()
			hosts.close()			
			linhas = linha

		else:

			try:
				host = open(curPath+'/hosts/'+sys.argv[1]+'.host', 'r')
				linha = host.readlines()
				host.close()

				response = sys.argv[1]

				for l in linha:
					linhas.append(l)

			except:
				print 'Arquivo '+sys.argv[1]+'.host nao encontrado.'	
				sys.exit()

		hosts = open('/etc/hosts', 'w')
		hosts.writelines(linhas)
		hosts.close()

	print response
	for l in linha:
		print l

