import hashlib,json,time
class Chain:
    def __init__(s): s.chain=[]; s.add(proof=100,prev='1')
    def h(s,b): return hashlib.sha256(json.dumps(b,sort_keys=True).encode()).hexdigest()
    def add(s,proof,prev=None,tx=None):
        b={'i':len(s.chain)+1,'t':time.time(),'tx':tx or [],'proof':proof,'prev':prev or s.h(s.chain[-1])}; s.chain.append(b); return b
    def pow(s,last):
        p=0
        while not hashlib.sha256(f'{last}{p}'.encode()).hexdigest().startswith('0000'): p+=1
        return p
    def valid(s): return all(s.chain[i]['prev']==s.h(s.chain[i-1]) for i in range(1,len(s.chain)))
c=Chain()
for n in range(3): c.add(c.pow(c.chain[-1]['proof']),tx=[{'from':'kin','to':'apostle','amt':n+1}])
print(len(c.chain),'blocks, valid:',c.valid()); c.chain[1]['tx']=[{'amt':999}]; print('after tamper valid:',c.valid())
