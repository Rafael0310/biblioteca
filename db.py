ADD_USER = '''
    INSERT INTO usuarios(nome, email, dt_cadastro) VALUES (%s, %s, %s);
'''

ADD_BOOK = '''
    INSERT INTO livros(titulo, autor, categoria, disp) VALUES (%s, %s, %s, %s);
'''

EMP_BOOK = '''
    INSERT INTO emprestimos(id_usuario, id_livro, data_emprestimo) VALUES (%s, %s, %s);
    INSERT INTO livros(disp) VALUES (0);
'''

DLV_BOOK = '''

'''