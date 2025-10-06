

def getBondPrice_E(face, couponRate, yc):
    """
    用年度即期利率 yc 定价（离散复利）：
    - face: 面值
    - couponRate: 年票息率，如 0.04
    - yc: 各年的年化即期利率列表，如 [0.010, 0.015, 0.020, 0.025, 0.030]
    说明：假设每年付息一次，最后一年现金流=票息+面值
    """
    price = 0.0
    n = len(yc)                   # 期限 = yc 的长度
    coupon = face * couponRate    # 每年票息

    for t, r in enumerate(yc, start=1):
        cf = coupon
        if t == n:                # 到期年加上面值
            cf += face
        price += cf / ((1 + r) ** t)

    return price

