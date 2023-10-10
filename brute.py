from foxfm import *
def brute(x):
    # 可以使用str(input_content,"utf8")对bytes类型进行转换
    # 使用bytes(input_content)对str进行转换，或者strings.encode()会将str转换为bytes类型
    table = string.ascii_letters+string.digits
    example = b"gr9BMrIea8ytbpya) == 55c2df00e0d25da626187371d814476ce6ffeb9ee535d62b23beedffed1f8d4b"
    # print(type(x))
    # x = str(x,"UTF-8")
    lent = len(example)
    x = x[-lent:]
    # print(x)
    # print(type(x))
    ans = x.split(") == ")
    part2 = ans[0]
    aim = ans[1]
    # print(part2,aim)
    for i in product(table,repeat=4):
        padding = "".join(i)
        pending = padding + part2
        # print(pending)
        test = hashlib.sha256(pending.encode()).hexdigest()
        if test == aim:
            print(padding)
            break


def test():
    brute("256(XXXX+OnwvYZOWEetdqRcp) == 201fef4cbd94ba720137875fbadee6bb5eb9f78a932b00af9db881048105151d")
# test()