
def getBondDuration(y, face, couponRate, m, ppy=1):
    """
    Macaulay Duration（按年计）:
    y   : 年化到期收益率，例如 0.03
    face: 面值
    couponRate: 年票息率，例如 0.04
    m   : 到期期限（年）
    ppy : 每年付息次数（1=年付，2=半年付，…）
    """
    N = int(m * ppy)              # 总期数
    r = y / ppy                   # 每期贴现率
    c = face * couponRate / ppy   # 每期票息

    # 债券价格 = 所有现金流现值之和（离散复利）
    if r == 0:
        # y=0 的极端情形
        price = c * N + face
        num = sum((t/ppy) * c for t in range(1, N + 1)) + (N/ppy) * face
        return num / price

    price = sum(c / ((1 + r) ** t) for t in range(1, N + 1)) + face / ((1 + r) ** N)

    # 加权时间的现值之和（时间用“年”，所以乘以 t/ppy）
    numerator = sum((t/ppy) * (c / ((1 + r) ** t)) for t in range(1, N + 1))
    numerator += (N/ppy) * (face / ((1 + r) ** N))

    return numerator / price

