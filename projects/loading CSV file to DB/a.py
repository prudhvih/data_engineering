import multiprocessing
import time

def mysleep(i):
    print(f'sleep for {i} sec')
    time.sleep(i)


def main():
    l = [1,2,3,4,5,6]

    pool = multiprocessing.Pool(4)
    pool.map(mysleep,l)


if __name__ == '__main__' :
    main()



new = (lambda x : sorted( list[2] , key= list[01]))



filter( list[] , key = lambda x : x%2 == 0)