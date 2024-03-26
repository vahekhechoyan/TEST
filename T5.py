def foo(n:int)->int:
    if n<10:
        return n
    else:
        return n%10 + foo(n//10)
    

print(foo(15678490))

# with lambda
foo=lambda n: 1 if n<10 else n%10 +foo(n//10)

print(foo(156784990))


# without recursive
def foo(n:int) -> int:

    sum_of_digit = 0

    while n > 0:

        sum_of_digit += n % 10

        n = n // 10

    return sum_of_digit

print(foo(15678490))