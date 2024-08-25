import sqlite3

# Armazenar na memória para pouco uso
# conn = sqlite3.connect(':memory:')

# Conectar a base de dados
conn = sqlite3.connect('customer.db')

# Criar um cursor
c = conn.cursor()

'''
# Criar uma tabela
# Tipos de DataBase: Null, Integer, Real, Text e Blob

c.execute("""Create Table customers (
          first_name text,
          last_name text,
          email text
          )
""")

----------------------------------------------------------------------------------

# Adicionar um item

c.execute("INSERT INTO customers Values ('Mary', 'Polletti', 'Mary@codemy.com')")

----------------------------------------------------------------------------------

# Adicionar vários itens

many_customers = [('Wes', 'Brown', 'wes@codemy.com'), 
                  ('Carlos', 'Silva', 'carlos@codemy.com'), 
                  ('Steph', 'Kuewa', 'steph@codemy.com')]

c.executemany("INSERT INTO customers VALUES(?, ?, ?)", many_customers)

----------------------------------------------------------------------------------

# Ver a base de dados

c.execute("SELECT * FROM customers")
c.fetchone() - Ver uma
c.fetchmany(3) - Ver uma quantia
print(c.fetchall)) - Ver tudo

print(c.fetchone()[0]) - Selecionar uma coisa de algo

----------------------------------------------------------------------------------

# Loop para deixar o banco mais bonito
 
items = c.fetchall()

for item in items:
    print(f'Nome: {item[0]}, Sobrenome: {item[1]}, e-mail: {item[2]}')

----------------------------------------------------------------------------------

# Usar rowid para pegar a posição de um objeto
    
c.execute("SELECT rowid, * FROM customers")

----------------------------------------------------------------------------------

# Comando para pesquisar algo mais especifico

c.execute("SELECT * FROM customers WHERE last_name ='Elder'")

# Comando para pesquisar algo mais especifico sem especificar completamente o que precisa

c.execute("SELECT * FROM customers WHERE email LIKE '%gmail.com'")

----------------------------------------------------------------------------------

# Atualizar alguma coisa (não melhor forma)

c.execute("UPDATE customers SET first_name = 'Matheus' WHERE last_name = 'Cazuche'")

# Atualizar alguma coisa com base no rowid (garantindo que não terá falha)

c.execute("UPDATE customers SET first_name = 'John' WHERE rowid = 1")

----------------------------------------------------------------------------------

# Deletar algo

c.execute("DELETE from customers Where email LIKE '%codemy.com'") 

----------------------------------------------------------------------------------

# Organizar

c.execute("SELECT rowid, * FROM customers ORDER BY rowid DESC")

c.execute("SELECT rowid, * FROM customers ORDER BY last_name")

----------------------------------------------------------------------------------

# Selecionar o banco de dados - AND/OR

c.execute("SELECT rowid, * FROM customers WHERE last_name LIKE 'Po%' AND ROWID = 3")

c.execute("SELECT rowid, * FROM customers WHERE last_name LIKE 'Po%' OR ROWID = 3")

----------------------------------------------------------------------------------

# Limitar o resultado

c.execute("SELECT rowid, * FROM customers LIMIT 2")

c.execute("SELECT rowid, * FROM customers ORDER BY rowid DESC LIMIT 2")

----------------------------------------------------------------------------------

# Deletar uma Tabela

c.execute("DROP TABLE customers")

'''

# Enviar nosso comando
conn.commit()

# Fechar a coneção
conn.close()

# Funções

def show_all() -> str:
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("SELECT rowid, * from customers")
    items = c.fetchall()
    for item in items:
        print(item)
    conn.commit()
    conn.close()


def add_one(first: str, last: str, email: str) -> None:
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("INSERT INTO customers VALUES (?, ?, ?)", (first, last, email))
    conn.commit()
    conn.close()


def delete_one(id: int) -> None:
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("DELETE from customers WHERE rowid = (?)", id)
    conn.commit()
    conn.close()


def add_many(list: list) -> None:
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.executemany("INSERT INTO customers Values (?, ?, ?)", (list))
    conn.commit()
    conn.close()

def email_lookup(email: str) -> str:
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("SELECT rowid, * from customers WHERE email = (?)", (email, ))
    itens = c.fetchall()
    for item in itens:
        print(item)
    conn.commit()
    conn.close()


# EM OUTRA .PY

import database

database.add_one('Matheus', 'Polletti', 'matheus@gmail.com')

database.delete_one('5')

stuff = [('Teste1', 'Sobrenome1', 'email1@gmail.com'), ('Teste2', 'Sobrenome2', 'email2@gmail.com')]
database.add_many(stuff)

database.show_all()

database.email_lookup('matheus@gmail.com')
