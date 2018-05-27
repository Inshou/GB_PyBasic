def clear():
    """
    Функция для очистки консоли перед выводом/вводом данных
    """
    print("\n" * 100)


def interface(commands, tasks, args=[]):
    """
    Интерфейс
    """

    alert = ''

    for key, command in commands.items():
        alert += '[{}] {}\n'.format(key, command)

    alert += '[q] Завершить работу\n\nВыберите действие: '

    answer = ''
    while answer not in ('q', 'Q'):
        answer = input(alert)
        clear()
        if answer in tasks:
            try:
                tasks[answer](args[answer][0])
            except:
                try:
                    tasks[answer](args[answer][0], args[answer][1])
                except:
                    tasks[answer]()
        elif answer in ('q', 'Q'):
            pass
        else:
            print('Указанная задача не найдена\n')

    print('Спасибо, за использования нашего программного обеспечения, удачи.')
