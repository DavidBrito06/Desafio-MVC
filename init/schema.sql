CREATE TABLE IF NOT EXISTS pessoa_fisica (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    renda_mensal REAL,
    idade INTEGER,
    nome_completo TEXT,
    celular TEXT,
    email TEXT,
    categoria TEXT,
    saldo REAL
);

CREATE TABLE IF NOT EXISTS pessoa_juridica (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    faturamento REAL,
    idade INTEGER,
    nome_fantasia TEXT,
    celular TEXT,
    email_corporativo TEXT,
    categoria TEXT,
    saldo REAL
);

INSERT INTO pessoa_fisica (renda_mensal, idade, nome_completo, celular, email, categoria, saldo)
VALUES
(5000.00, 35, 'João da Silva', '9999-8888', 'joao@example.com', 'Categoria A', 10000.00),
(4000.00, 45, 'Maria Oliveira', '7777-6666', 'maria@example.com', 'Categoria B', 15000.00),
(6000.00, 28, 'Pedro Santos', '5555-4444', 'pedro@example.com', 'Categoria C', 8000.00);

INSERT INTO pessoa_juridica (faturamento, idade, nome_fantasia, celular, email_corporativo, categoria, saldo)
VALUES
(100000.00, 10, 'Empresa XYZ', '1111-2222', 'contato@empresa.com', 'Categoria A', 50000.00),
(80000.00, 5, 'Empresa ABC', '3333-4444', 'contato@abc.com', 'Categoria B', 70000.00),
(120000.00, 8, 'Empresa 123', '5555-6666', 'contato@123.com', 'Categoria C', 90000.00);