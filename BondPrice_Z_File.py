

def getBondPrice_Z(face, couponRate, times, yc):
    """
    不规则时点定价（离散复利）:
    - face: 面值
    - couponRate: 年票息率（如 0.04）
    - times: 每笔现金流发生的时间（年），可含小数，如 [1, 1.5, 3, 4, 7]
    - yc: 对应每个时点的年化即期利率列表（与 times 一一对应）
    规则：每个时点付票息，最后一个时点再加面值
    """
    price = 0.0
    coupon = face * couponRate
    n = len(times)

    for i, (t, r) in enumerate(zip(times, yc)):
        cf = coupon
        if i == n - 1:            # 最后一期加上面值
            cf += face
        price += cf / ((1 + r) ** t)
    return price
