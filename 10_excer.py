def run():
    num = 0
    while num < 100:
        # num+=1
        # print(num)
        # if num == 10:
        #     break

        num+=1
        if num % 2 != 0:
            continue
        print(num)

if __name__ == '__main__':
    run()