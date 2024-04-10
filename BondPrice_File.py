def getBondPrice(y, face, couponRate, m, ppy=1):
    pvcfsum = 0
    cf = face * couponRate / ppy
    for n in range(1, m*ppy):
        df = (1+y/ppy)**(-n)
        pvcf = cf*df
        pvcfsum = pvcfsum+pvcf
    bondPrice = pvcfsum + face/(1+y/ppy)**(m*ppy)
    return(bondPrice)