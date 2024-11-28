CREATE DATABASE biblioteca;

USE biblioteca;

CREATE TABLE usuarios(
	id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    dt_cadastro DATE NOT NULL
);

CREATE TABLE livros(
	id INT PRIMARY KEY AUTO_INCREMENT,
    titulo VARCHAR(255) NOT NULL,
    autor VARCHAR(255) NOT NULL,
    categoria VARCHAR(255) NOT NULL,
    disp BOOL NOT NULL
);

CREATE TABLE emprestimo(
	id_emprestimo INT PRIMARY KEY,
    id_usuario INT NOT NULL,
    id_livros INT NOT NULL,
    data_emprestimo DATE NOT NULL,
    data_devolucao DATE NOT NULL,
	FOREIGN KEY (id_usuario) REFERENCES usuarios (id),
    FOREIGN KEY (id_livros) REFERENCES livros(id)
);