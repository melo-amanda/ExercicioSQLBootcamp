import sqlite3

conexao = sqlite3.connect('BancoExercicio')
cursor = conexao.cursor()

cursor.execute('PRAGMA foreign_keys = ON')

#Crie uma tabela chamada "alunos" com os seguintes campos: id (inteiro), nome (texto), idade (inteiro) e curso (texto)
# cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR(100), idade INT, curso VARCHAR(100))')

#Insira pelo menos 5 registros de alunos na tabela que você criou no exercício anterior.
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(1, "Amanda", 23, "Eng. de Producao")')
# cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(2, "Nicholas", 29, "Eng. Mecânica")')
# cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(3, "Mateus", 24, "Eng. Mecânica")')
# cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(4, "Carol", 23, "Eng. de Produção")')
# cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(5, "Vivian", 23, "Administração")')

#Selecionar todos os registros da tabela "alunos".
todos_dados = cursor.execute('SELECT * FROM alunos')

#Selecionar o nome e a idade dos alunos com mais de 20 anos.
alunos_novos = cursor.execute('SELECT nome, idade FROM alunos WHERE idade > 20')

#Selecionar os alunos do curso de "Engenharia" em ordem alfabética.
engenheiros = cursor.execute('SELECT * FROM alunos WHERE curso LIKE "%Eng.%" ORDER BY nome')

#Contar o número total de alunos na tabela
total = cursor.execute('SELECT COUNT(id) FROM alunos')

#Atualize a idade de um aluno específico na tabela.
# cursor.execute('UPDATE alunos SET idade=25 WHERE nome="Mateus"')

#Remova um aluno pelo seu ID
# cursor.execute('DELETE FROM alunos WHERE id=2')

#Crie uma tabela chamada "clientes" com os campos: id (chave primária), nome (texto), idade (inteiro) e saldo (float). Insira alguns registros de clientes na tabela.
# cursor.execute('CREATE TABLE clientes(id INT PRIMARY KEY, nome VARCHAR(100), idade INT, saldo FLOAT)')

# cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(1, "Rogerio", 40, 4000)')
# cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(2, "Marcelo", 50, 10000)')
# cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(3, "Simone", 50, 8000)')
# cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(4, "Silvia", 51, 5000)')
# cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(5, "Lais", 30, 1000)')

#Selecione o nome e a idade dos clientes com idade superior a 30 anos.
mais_velhos = cursor.execute('SELECT nome,idade FROM clientes WHERE idade>30')

#Calcule o saldo médio dos clientes.
saldo_medio = cursor.execute('SELECT AVG(saldo) FROM clientes')

#Encontre o cliente com o saldo máximo.
saldo_max = cursor.execute('SELECT MAX(saldo) FROM clientes')

#Conte quantos clientes têm saldo acima de 1000.
qtd_maior = cursor.execute('SELECT COUNT(id) FROM clientes WHERE saldo>1000')

#Atualize o saldo de um cliente específico.
# cursor.execute('UPDATE clientes SET saldo=2000 WHERE nome="Rogerio"')

#Remova um cliente pelo seu ID.
# cursor.execute('DELETE FROM clientes WHERE id=4')

#Crie uma segunda tabela chamada "compras" com os campos: id (chave primária), cliente_id (chave estrangeira referenciando o id da tabela "clientes"), produto (texto) e valor (real). Insira algumas compras associadas a clientes existentes na tabela "clientes". Escreva uma consulta para exibir o nome do cliente, o produto e o valor de cada compra.
# cursor.execute('CREATE TABLE compras(id INT PRIMARY KEY, cliente_id INT, produto VARCHAR(100), valor FLOAT, FOREIGN KEY(cliente_id) REFERENCES clientes(id))')
# cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES(1, 3, "café", 10)')
# cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES(2, 1, "frango", 40)')
# cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES(3, 2, "chocolate", 3)')

join = cursor.execute('SELECT nome, produto, valor FROM clientes INNER JOIN compras ON clientes.id = compras.cliente_id')

conexao.commit()
conexao.close()

#cursor.execute('CREATE TABLE usuarios(id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR(100))')
#cursor.execute('ALTER TABLE usuarios RENAME TO usuario')
#cursor.execute('ALTER TABLE usuario ADD COLUMN telefoni INT')
#cursor.execute('ALTER TABLE usuario RENAME COLUMN telefoni TO telefone')
# cursor.execute('DROP TABLE alunos')
#cursor.execute('INSERT INTO usuario(id,nome,endereco,email,telefone) VALUES(1,"Isadora","França","isa@gmail.com",123456)')
#cursor.execute('INSERT INTO usuario(id,nome,endereco,email,telefone) VALUES(2,"Amanda","Brasil","amanda@gmail.com",37164)')
#cursor.execute('INSERT INTO usuario(id,nome,endereco,email,telefone) VALUES(3,"Nicholas","Canada","nicholas@gmail.com",845473)')
#cursor.execute('DELETE FROM usuario where id=1')
# cursor.execute('UPDATE usuario SET endereco="Rio de Janeiro" WHERE nome="Nicholas"')