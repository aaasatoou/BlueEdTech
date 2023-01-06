CREATE SCHEMA projeto_1;

USE projeto_1;

CREATE TABLE candidato(
	id INT NOT NULL AUTO_INCREMENT,
    nome TEXT,
    cpf VARCHAR(11),
    estado ENUM('AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO'),
    nascimento DATE,
    pretensao FLOAT,
    telefone VARCHAR(10), # DDD + 8 digitos
	email TEXT,
    
    PRIMARY KEY(id)
);

CREATE TABLE recrutador(
	id INT NOT NULL AUTO_INCREMENT,
    nome TEXT,
    unidade TEXT,
    
    PRIMARY KEY(id)
);

CREATE TABLE vaga(
	id INT NOT NULL AUTO_INCREMENT,
    nome_vaga TEXT,
	requisitos TEXT,
    tecnologia TEXT,
    data_abertura DATE,
    setor TEXT,
    recrutador_id INT,
    
    PRIMARY KEY(id),
    FOREIGN KEY (recrutador_id) REFERENCES recrutador(id)
);

CREATE TABLE aplicacoes(
	id INT NOT NULL AUTO_INCREMENT,
    `status` ENUM('cancelado', 'finalizado'),
	candidato_id INT,
    vaga_id INT,
    nota_testes TINYINT, # Espera-se que as notas seja tratados no front-end antes de inseridas aqui.
    
    PRIMARY KEY(id),
    FOREIGN KEY (candidato_id) REFERENCES candidato(id),
    FOREIGN KEY (vaga_id) REFERENCES vaga(id)
);

CREATE TABLE etapas(
	cadastro DATE,
    entrevista_rh DATE,
    entrevista_gestor DATE,
    proposta DATE,
    contratacao DATE,
    aplicacoes_id INT,
    
    FOREIGN KEY (aplicacoes_id) REFERENCES aplicacoes(id),
    PRIMARY KEY(aplicacoes_id)
);