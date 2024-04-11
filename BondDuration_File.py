def getBondDuration(y, face, couponRate, m, ppy = 1):
    pvcfsum = 0
    pvcftsum = 0
    cf = face * couponRate / ppy
    for n in range(1, m*ppy+1):
        df = (1+y/ppy)**(-n)
        pvcf = cf*df
        pvcft = cf*df*n/ppy
        pvcfsum += pvcf
        pvcftsum += pvcft
    bondPrice = pvcfsum + face/(1+y/ppy)**(m*ppy)
    bondDuration = (pvcftsum+(face/(1+y/ppy)**(m*ppy))*m)/bondPrice
    return(bondDuration)