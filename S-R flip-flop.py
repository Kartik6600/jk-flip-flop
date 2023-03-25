def NOT(A): return ~A+2     
def OR(A,B): return A|B     
def AND(A,B): return A&B
def SR(S,R,Qp):
    Qn=OR(S,AND(NOT(R),Qp))
    
    if S==0 and R==0 :
        return Qn,'Hold State'
    elif S==0 and R==1 :
        return Qn,'Reset State'
    elif S==1 and R==0 :
        return Qn,'Set State'
    elif S==1 and R==1 :
        return Qn,'Intermediate State'

print('SR Flip Flop')
print('| S | R | Qp| Qn')
print('| 0 | 0 | 0 |',SR(0,0,0))
print('| 0 | 0 | 1 |',SR(0,0,1))
print('| 0 | 1 | 0 |',SR(0,1,0))
print('| 0 | 1 | 1 |',SR(0,1,1))
print('| 1 | 0 | 0 |',SR(1,0,0))
print('| 1 | 0 | 1 |',SR(1,0,1))
print('| 1 | 1 | 0 |',SR(1,1,0))
print('| 1 | 1 | 1 |',SR(1,1,1))
