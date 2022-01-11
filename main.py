from engine.linkedin import Linkedin

text ="Olá, tudo bem?\n\nEu agradeço muito pela oportunidade, mas no momento estou em um projeto muito importante para minha carreira.\n\nMas eu gostaria de manter o contato para troca de conhecimento, parceria e trabalho.\n\nObrigado pela oportunidade."

linkedin = Linkedin()
linkedin.login()
#linkedin.accept_connections()
linkedin.answer_job_invitations(text)
input("Pressione qualquer tecla para sair")