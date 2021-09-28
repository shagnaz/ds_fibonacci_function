list = []
def find_fibonacci(x: int) -> bool:
    """
    Menemukan bilangan bulat x di dalam suatu deret fibonacci.
    Apabila x ada di dalam suatu deret fibonacci, maka kembalikan True.
    Jika tidak ada, maka kembalikan False
    """
    # write your code here
    f0 = 0 #seed fibonacci
    f1 = 1 #seed fibonacci
    list.extend([f0,f1])
    for idx, value in enumerate(list):
        if value <= x:
            fibo = value + list[idx+1]
            list.append(fibo)
   
    if (x in list):
        return True
    else:
        return False

if __name__ == "__main__":
    """Jalankan beberapa test-case di bawah sini
    """
    print(find_fibonacci(1))
    print(find_fibonacci(10))
    print(find_fibonacci(11))
