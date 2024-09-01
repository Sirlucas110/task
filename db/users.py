import sqlite3

# Conexão com o banco de dados (ou criação se não existir)
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Criação da tabela 'users'
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL
)
''')

# Inserção de alguns usuários de exemplo
cursor.execute("INSERT INTO users (name, email) VALUES ('John Doe', 'john.doe@example.com')")
cursor.execute("INSERT INTO users (name, email) VALUES ('Jane Smith', 'jane.smith@example.com')")

# Salvando as alterações e fechando a conexão
conn.commit()
conn.close()
