import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import pandas as pd
from tkinter import filedialog

class DatabaseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Программа с интерактивным меню")

        self.main_menu = tk.Menu(self.root)
        self.root.config(menu=self.main_menu)

        self.database_menu = tk.Menu(self.main_menu, tearoff=0)
        self.main_menu.add_cascade(label="База данных", menu=self.database_menu)
        self.database_menu.add_command(label="Создать базу данных", command=self.create_database)
        self.database_menu.add_command(label="Создать таблицу", command=self.create_table)

        self.data_menu = tk.Menu(self.main_menu, tearoff=0)
        self.main_menu.add_cascade(label="Данные", menu=self.data_menu)
        self.data_menu.add_command(label="Ввести стек", command=self.input_stack)
        self.data_menu.add_command(label="Вывести данные", command=self.display_data)
        self.data_menu.add_command(label="Сохранить в Excel", command=self.save_to_excel)

    def create_database(self):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="ваш_пользователь",
                password="ваш_пароль"
            )
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS mydatabase")
            messagebox.showinfo("Успех", "База данных успешно создана")
        except mysql.connector.Error as err:
            messagebox.showerror("Ошибка", f"Ошибка при создании базы данных: {err}")
        finally:
            cursor.close()
            connection.close()

    def create_table(self):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="ваш_пользователь",
                password="ваш_пароль",
                database="mydatabase"
            )
            cursor = connection.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS stack_data (ID INT AUTO_INCREMENT PRIMARY KEY, "
                           "StackText TEXT)")
            messagebox.showinfo("Успех", "Таблица успешно создана")
        except mysql.connector.Error as err:
            messagebox.showerror("Ошибка", f"Ошибка при создании таблицы: {err}")
        finally:
            cursor.close()
            connection.close()

    def input_stack(self):
        input_window = tk.Toplevel(self.root)
        input_window.title("Ввод стека")
        input_frame = ttk.Frame(input_window)
        input_frame.grid(row=0, column=0, padx=10, pady=10)

        ttk.Label(input_frame, text="Введите элементы стека (через запятую):").grid(row=0, column=0, padx=5, pady=5)
        self.stack_entry = ttk.Entry(input_frame)
        self.stack_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Button(input_frame, text="Сохранить в MySQL", command=self.save_stack_to_mysql).grid(row=1, column=0, columnspan=2, padx=5, pady=10)

    def save_stack_to_mysql(self):
        stack_text = self.stack_entry.get()
        stack_list = stack_text.split(',')

        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="ваш_пользователь",
                password="ваш_пароль",
                database="mydatabase"
            )
            cursor = connection.cursor()
            for item in stack_list:
                cursor.execute("INSERT INTO stack_data (StackText) VALUES (%s)", (item.strip(),))
            connection.commit()
            messagebox.showinfo("Успех", "Стек успешно сохранен в MySQL")
        except mysql.connector.Error as err:
            messagebox.showerror("Ошибка", f"Ошибка при вставке данных в MySQL: {err}")
        finally:
            cursor.close()
            connection.close()

    def display_data(self):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="ваш_пользователь",
                password="ваш_пароль",
                database="mydatabase"
            )
            query = "SELECT * FROM stack_data"
            df = pd.read_sql(query, connection)

            data_window = tk.Toplevel(self.root)
            data_window.title("Данные из MySQL")
            text_widget = tk.Text(data_window)
            text_widget.insert(tk.END, df.to_string(index=False))
            text_widget.pack()
        except mysql.connector.Error as err:
            messagebox.showerror("Ошибка", f"Ошибка при запросе данных из MySQL: {err}")
        finally:
            connection.close()

    def save_to_excel(self):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="ваш_пользователь",
                password="ваш_пароль",
                database="mydatabase"
            )
            query = "SELECT * FROM stack_data"
            df = pd.read_sql(query, connection)

            file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel Files", "*.xlsx")])
            if file_path:
                df.to_excel(file_path, index=False)
                messagebox.showinfo("Успех", f"Данные успешно сохранены в {file_path}")
        except mysql.connector.Error as err:
            messagebox.showerror("Ошибка", f"Ошибка при запросе данных из MySQL: {err}")
        finally:
            connection.close()

if __name__ == "__main__":
    root = tk.Tk()
    app = DatabaseApp(root)
    root.mainloop()