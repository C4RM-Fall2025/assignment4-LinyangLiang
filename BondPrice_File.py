

def getBondPrice(y, face, couponRate, m, ppy=1):
    """
    y: 年化到期收益率，例如 0.03
    face: 面值
    couponRate: 年票息率，例如 0.04
    m: 期限(年)
    ppy: 每年付息次数(1=年付, 2=半年付, ...)
    """
    N = int(m * ppy)             # 总期数
    r = y / ppy                  # 每期折现率
    c = face * couponRate / ppy  # 每期票息

    # 年金现值 + 面值现值（离散复利）
    pv_coupons = c * (1 - (1 + r) ** (-N)) / r if r != 0 else c * N
    pv_face    = face / ((1 + r) ** N)
    return pv_coupons + pv_face
