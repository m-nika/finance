import sqlite3

conn = sqlite3.connect('finances.db')
cursor = conn.cursor()


# cursor.execute("""CREATE TABLE finances(
# id INTEGER PRIMARY KEY,
# type TEXT,
# amount INTEGER,
# category TEXT
# )""")


def enter_income():
    type = 'income'
    amount = float(input('enter your income: '))
    category = input('enter category: ')
    cursor.execute('INSERT INTO finances (type, amount, category) VALUES (?, ?, ?)', ('income', amount, category))
    conn.commit()


def enter_expense():
    type = 'expenses'
    amount = float(input('enter your expense: '))
    category = input('enter category: ')
    cursor.execute('INSERT INTO finances (type, amount, category) VALUES (?, ?, ?)', ('expenses', amount, category))
    conn.commit()


def get_balance():
    cursor.execute('SELECT SUM(amount) FROM finances WHERE type = "income"')
    income_sum = cursor.fetchone()[0] or 0
    cursor.execute('SELECT SUM(amount) FROM finances WHERE type = "expenses"')
    expenses_sum = cursor.fetchone()[0] or 0
    balance = income_sum - expenses_sum  # Fix the variable name here
    print(f'Your balance: {balance}')


def get_all_incomes():
    cursor.execute('SELECT * FROM finances WHERE type="income"')
    incomes = cursor.fetchall()
    print('your income: ')
    print('id\ttype\tamount\tcategory')
    for income in incomes:
        print(f'{income[0]}\t{income[1]}\t{income[2]}\t{income[3]}')


def get_all_expenses():
    cursor.execute('SELECT * FROM finances WHERE type="expenses"')
    expenses = cursor.fetchall()
    print('your expenses: ')
    print('id\ttype\tamount\tcategory')
    for expense in expenses:
        print(f'{expense[0]}\t{expense[1]}\t${expense[2]}\t{expense[3]}')


def delete():
    record_id = int(input('enter the id of the record you wish to delete: '))
    cursor.execute('DELETE FROM finances WHERE id=?', (record_id,))
    conn.commit()


def update():
    record_id = int(input('enter the id of the record you wish to update: '))
    new_type = input('enter type(income/expenses): ')
    new_amount = float(input('enter amount: '))
    new_category = input('enter category: ')
    cursor.execute('UPDATE Finances SET type=?, amount=?, category=? WHERE id=?',
                   (new_type, new_amount, new_category, record_id))
    conn.commit()


while True:
    print('1.enter income')
    print('2.enter expense')
    print('3.get balance')
    print('4.get all incomes')
    print('5.get all expenses')
    print('6.delete')
    print('7.update')
    print('8.close')

    choice = input('enter your choice (1 - 8): ')

    if choice == '1':
        enter_income()
    elif choice == '2':
        enter_expense()
    elif choice == '3':
        get_balance()
    elif choice == '4':
        get_all_incomes()
    elif choice == '5':
        get_all_expenses()
    elif choice == '6':
        delete()
    elif choice == '7':
        update()
    elif choice == '8':
        print('exiting finance file')
        break
    else:
        print('enter a number from 1 to 8')
