def solution(numer1, denom1, numer2, denom2):
    answer = []
    y=denom1 * denom2

    z=numer1*denom2+numer2*denom1

    for _ in range(min(z, y), 0, -1):
        if z%_ == y%_ == 0:
            x=_
            break


    a, b=z/x , y/x
    answer = [a, b]
    
    return answer