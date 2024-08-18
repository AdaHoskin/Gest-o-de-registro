import sqlite3

# Nome do banco de dados
DB_NAME = 'tarefas.db'

# Função para criar o banco de dados e a tabela
def criar_tabela():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tarefas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                descricao TEXT NOT NULL,
                status TEXT NOT NULL
            )
        ''')
        conn.commit()

# Função para adicionar uma tarefa
def adicionar_tarefa(descricao, status):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO tarefas (descricao, status)
            VALUES (?, ?)
        ''', (descricao, status))
        conn.commit()
        print(f'Tarefa adicionada: {descricao} - {status}')

# Função para remover uma tarefa
def remover_tarefa(tarefa_id):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            DELETE FROM tarefas WHERE id = ?
        ''', (tarefa_id,))
        conn.commit()
        print(f'Tarefa com ID {tarefa_id} removida.')

# Função para atualizar uma tarefa
def atualizar_tarefa(tarefa_id, nova_descricao, novo_status):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE tarefas
            SET descricao = ?, status = ?
            WHERE id = ?
        ''', (nova_descricao, novo_status, tarefa_id))
        conn.commit()
        print(f'Tarefa com ID {tarefa_id} atualizada.')

# Função para listar todas as tarefas
def listar_tarefas():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM tarefas')
        tarefas = cursor.fetchall()
        if tarefas:
            print('Tarefas:')
            for tarefa in tarefas:
                print(f'ID: {tarefa[0]}, Descrição: {tarefa[1]}, Status: {tarefa[2]}')
        else:
            print('Nenhuma tarefa encontrada.')

# Função principal para interação com o usuário
def main():
    criar_tabela()

    while True:
        print('\nGerenciamento de Tarefas')
        print('1. Adicionar tarefa')
        print('2. Remover tarefa')
        print('3. Atualizar tarefa')
        print('4. Listar tarefas')
        print('5. Sair')

        escolha = input('Escolha uma opção: ')

        if escolha == '1':
            descricao = input('Descrição da tarefa: ')
            status = input('Status da tarefa: ')
            adicionar_tarefa(descricao, status)
        elif escolha == '2':
            tarefa_id = int(input('ID da tarefa a remover: '))
            remover_tarefa(tarefa_id)
        elif escolha == '3':
            tarefa_id = int(input('ID da tarefa a atualizar: '))
            nova_descricao = input('Nova descrição: ')
            novo_status = input('Novo status: ')
            atualizar_tarefa(tarefa_id, nova_descricao, novo_status)
        elif escolha == '4':
            listar_tarefas()
        elif escolha == '5':
            break
        else:
            print('Opção inválida. Tente novamente.')

if __name__ == '__main__':
    main()