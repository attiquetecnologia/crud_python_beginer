# funções de crud
from db import conn

def create(tarefa):
    """ adiciona uma nova tarefa """
    conn.execute("insert into tarefa (tarefa, concluido) values (?, 0)", (tarefa, ))
    conn.commit()

def delete(id):
    """ remove a tarefa da tabela """
    conn.execute("delete from tarefa where id = ?", (id, ))
    conn.commit()

def update(id):
    """ marca a tarefa como concluida """
    conn.execute("update tarefa set concluido = 1 where id = ?", (id, ))
    conn.commit()

def find_all(): # retorna um cursor
    """ retorna a lista de tarefas cadastras """
    return conn.execute("select id, tarefa, concluido from tarefa")