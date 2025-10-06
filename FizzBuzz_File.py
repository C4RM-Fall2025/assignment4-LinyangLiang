

def FizzBuzz(start, finish):
    """
    生成从 start 到 finish（含两端）的 FizzBuzz 列表：
    - 3 的倍数 -> "fizz"
    - 5 的倍数 -> "buzz"
    - 15 的倍数 -> "fizzbuzz"
    - 否则返回整数本身
    """
    outlist = []
    for n in range(start, finish + 1):
        if n % 15 == 0:
            outlist.append("fizzbuzz")
        elif n % 3 == 0:
            outlist.append("fizz")
        elif n % 5 == 0:
            outlist.append("buzz")
        else:
            outlist.append(n)
    return outlist

