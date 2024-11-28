ADD_USER = '''
    INSERT INTO usuarios(nome, email, dt_cadastro) VALUES (%s, %s, %s)
'''

ADD_BOOK = '''
    INSERT INTO livros(titulo, autor, categoria, disp) VALUES (%s, %s, %s, %s)
'''