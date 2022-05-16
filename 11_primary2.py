def prime(num):

    for i in range(1, num + 1):
        if num == 1:
            return False
        if num % i == 0:
            return True

def run():
    num = int(input('Ingresa un numero: '))
    if prime(num):
        print('SI 😀')
    else:
        print('NO 🥵')

if __name__ == '__main__':
    run()