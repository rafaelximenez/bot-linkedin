from engine.linkedin import Linkedin

linkedin = Linkedin()
linkedin.login()
linkedin.search_jobs('Engenheiro de dados')
input("Pressione qualquer tecla para sair")