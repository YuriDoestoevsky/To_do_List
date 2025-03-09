import sqlite3

conn = sqlite3.connect('Todo.db')


def create_table():
      conn = sqlite3.connect('Todo.db')
      conn.execute(
               '''
               CREATE TABLE IF NOT EXISTS Todo
               (
                  task TEXT,
                  time TEXT
               )
               '''
               )
      conn.commit()
      conn.close()
      
def add_task(task, time):
      conn = sqlite3.connect('Todo.db')
      conn.execute(
               '''
               INSERT INTO Todo (task, time)
               VALUES (?, ?)
               ''', (task, time)
               )
      conn.commit()
      conn.close()
      
def get_tasks():
    conn = sqlite3.connect('Todo.db')
    cursor = conn.cursor()
    cursor.execute('SELECT task, time FROM Todo ORDER BY time DESC')
    tasks = cursor.fetchall()
    conn.close()
    return tasks

def delete(task):
   conn = sqlite3.connect('Todo.db')
   cursor = conn.cursor()
   cursor.execute('DELETE FROM Todo WHERE task = ?', (task,))
   conn.commit()
   conn.close()
   