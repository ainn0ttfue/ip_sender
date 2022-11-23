import os
import re
import sys

args = list(sys.argv)
IPV4_PATTERN = "^(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"

if __name__ == "__main__":
    if len(args) > 1 and args[1] in ['-c', '-s', '--help']:
        if args[1] in ('-c', '-s'):
            try:
                host_arg_id = args.index('-h')
                server_ip = args[host_arg_id + 1]

                if not re.match(IPV4_PATTERN, server_ip):
                    print('Неправильный формат IP адреса сервера')
                    sys.exit()

                port_arg_id = args.index('-p')
                server_port = args[port_arg_id + 1]

                if not (str(server_port).isdigit() and 65535 >= int(server_port) > 1023):
                    print('Ошибка: неправильно указан порт')
                    sys.exit()

                if args[1] == '-c':
                    print('Запуск клиента...')
                    os.system(f'python client.py {server_ip} {server_port}')
                else:
                    print('Запуск сервера...')

                    os.system(f'python server.py {server_ip} {server_port}')

            except (ValueError, IndexError):
                print('Ошибка: неправильная инициализация. Используйте --help для вывода справки')
        else:
            print('Запуск клиента: \n'
                  '>> python3 main.py -c -h 127.0.0.1 -p 65432 \n'
                  'Запуск сервера:\n'
                  '>> python3 main.py -s -h 127.0.0.1 -p 65432 \n'
                  '(вместо 127.0.0.1 укажите адрес сервера, порт можно указать любой свободный)')
    else:
        print('Используйте ключ --help для вывода справки')
