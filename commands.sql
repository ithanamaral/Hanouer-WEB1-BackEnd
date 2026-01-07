-- database: ./db.sqlite
CREATE TABLE usuarios(
    "name" TEXT,
    "CPF" TEXT NOT NULL UNIQUE PRIMARY KEY,
    "email" TEXT NOT NULL UNIQUE ,
    "password" TEXT NOT NULL);

CREATE TABLE pedidos(
    "id_pedido" INTEGER NOT NULL UNIQUE PRIMARY KEY,
    "data_pedido" TEXT NOT NULL,
    "valor_total" REAL NOT NULL,
    
    "CPF_fk_Usuario" TEXT NOT NULL,
    FOREIGN KEY("CPF_fk_Usuario") 
        REFERENCES usuarios("CPF")
        ON DELETE CASCADE
);

CREATE TABLE produtos(
    "id_produto" INTEGER NOT NULL UNIQUE PRIMARY KEY,
    "name" TEXT NOT NULL,
    "preco" REAL NOT NULL);

CREATE TABLE serviços(  
    "id_serviço" INTEGER NOT NULL UNIQUE PRIMARY KEY,
    "name" TEXT NOT NULL,
    "preco" REAL NOT NULL);


CREATE TABLE Item_Pedido_Serviço(
    "Quantidade" INTEGER,
    "Preço_unitário" REAL,
    "id_item" PRIMARY KEY,
    "id_fk_pedido" INTEGER NOT NULL,
    "id_fk_serviço" INTEGER NOT NULL,
    FOREIGN KEY("id_fk_pedido") 
        REFERENCES pedidos("id_pedido")
        ON DELETE CASCADE,
    FOREIGN KEY("id_fk_serviço") 
        REFERENCES serviços("id_serviço")
        ON DELETE CASCADE
);


CREATE TABLE Item_Pedido_Produto(
    "Quantidade" INTEGER,
    "Preço_unitário" REAL,
    "id_item" PRIMARY KEY,
    "id_fk_pedido" INTEGER NOT NULL,
    "id_fk_produto" INTEGER NOT NULL,
    FOREIGN KEY("id_fk_pedido") 
        REFERENCES pedidos("id_pedido")
        ON DELETE CASCADE,
    FOREIGN KEY("id_fk_produto") 
        REFERENCES produtos("id_produto")
        ON DELETE CASCADE
);

-- Add dados de teste
INSERT INTO usuarios (name, CPF, email, password) VALUES ('Alice Silva', '12345678901', 'alice.silva@example.com', 'senha123');
INSERT INTO pedidos(id_pedido, data_pedido, valor_total, CPF_fk_Usuario) VALUES (1, '2024-06-01', 150.00, '12345678901');
INSERT INTO produtos (id_produto, name, preco) VALUES (1, 'Camiseta', 50.00);
INSERT INTO Item_Pedido_Produto (id_fk_pedido, id_fk_produto, quantidade, preço_unitário)
VALUES (1, 1, 1, 50.00);
-- Não vai add por que não existe
INSERT INTO Item_Pedido_Produto (id_fk_pedido, id_fk_produto, quantidade, preço_unitário)
VALUES (2, 2, 1, 50.00);


INSERT INTO usuarios (name, CPF, email, password) VALUES ('Íthan P. Amaral', '10781629640', 'ithanamaral@gmail.com', 'senha123');