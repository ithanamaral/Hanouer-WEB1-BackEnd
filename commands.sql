-- database: ./db.sqlite
CREATE TABLE usuarios(
    "nome" TEXT,
    "CPF" TEXT NOT NULL UNIQUE PRIMARY KEY,
    "email" TEXT NOT NULL UNIQUE ,
    "senha" TEXT NOT NULL);

CREATE TABLE pedidos(
    "ID_Pedido" INTEGER NOT NULL UNIQUE PRIMARY KEY,
    "Data_Pedido" TEXT NOT NULL,
    "Valor_Total" REAL NOT NULL,
    
    "CPF_fk_Usuario" TEXT NOT NULL,
    FOREIGN KEY("CPF_fk_Usuario") 
        REFERENCES usuarios("CPF")
        ON DELETE CASCADE
);

CREATE TABLE produtos(
    "ID_Produto" INTEGER NOT NULL UNIQUE PRIMARY KEY,
    "Nome" TEXT NOT NULL,
    "Preco" REAL NOT NULL);

CREATE TABLE serviços(  
    "ID_Serviço" INTEGER NOT NULL UNIQUE PRIMARY KEY,
    "Nome" TEXT NOT NULL,
    "Preco" REAL NOT NULL);


CREATE TABLE Item_Pedido_Serviço(
    "Quantidade" INTEGER,
    "Preço_unitário" REAL,
    "ID_item" PRIMARY KEY,
    "ID_fk_Pedido" INTEGER NOT NULL,
    "ID_fk_Serviço" INTEGER NOT NULL,
    FOREIGN KEY("ID_fk_Pedido") 
        REFERENCES pedidos("ID_Pedido")
        ON DELETE CASCADE,
    FOREIGN KEY("ID_fk_Serviço") 
        REFERENCES serviços("ID_Serviço")
        ON DELETE CASCADE
);


CREATE TABLE Item_Pedido_Produto(
    "Quantidade" INTEGER,
    "Preço_unitário" REAL,
    "ID_item" PRIMARY KEY,
    "ID_fk_Pedido" INTEGER NOT NULL,
    "ID_fk_Produto" INTEGER NOT NULL,
    FOREIGN KEY("ID_fk_Pedido") 
        REFERENCES pedidos("ID_Pedido")
        ON DELETE CASCADE,
    FOREIGN KEY("ID_fk_Produto") 
        REFERENCES produtos("ID_Produto")
        ON DELETE CASCADE
);

-- Add dados de teste
INSERT INTO usuarios (nome, CPF, email, senha) VALUES ('Alice Silva', '12345678901', 'alice.silva@example.com', 'senha123');
INSERT INTO pedidos(ID_Pedido, Data_Pedido, Valor_Total, CPF_fk_Usuario) VALUES (1, '2024-06-01', 150.00, '12345678901');
INSERT INTO produtos (ID_Produto, Nome, Preco) VALUES (1, 'Camiseta', 50.00);
INSERT INTO Item_Pedido_Produto (ID_fk_Pedido, ID_fk_Produto, Quantidade, Preço_unitário)
VALUES (1, 1, 1, 50.00);
-- Não vai add por que não existe
INSERT INTO Item_Pedido_Produto (ID_fk_Pedido, ID_fk_Produto, Quantidade, Preço_unitário)
VALUES (2, 2, 1, 50.00);


INSERT INTO usuarios (nome, CPF, email, senha) VALUES ('Íthan P. Amaral', '10781629640', 'ithanamaral@gmail.com', 'senha123');
