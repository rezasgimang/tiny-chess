import os,json,urllib.request as U
V=(0,100,320,330,500,900,0);M=20000
D=[(),(),(33,31,18,14,-14,-18,-31,-33),(15,17,-15,-17),(1,-1,16,-16)];D+=[D[3]+D[4]]*2
P=[[0]*64 for _ in range(8)]
for i in range(64):
 r=i//8;f=i&7;u=min(f,7-f)+min(r,7-r)
 P[1][i]=(0,0,4,8,14,24,40,0)[r]
 P[2][i]=6*u-20
 P[3][i]=4*u-8
 P[6][i]=(20,25,10,0,0,10,25,20)[f] if r==0 else-15*r
G=[s for s in range(128)if not s&136];W={0:13,7:14,112:7,119:11,4:12,116:3}
b=[0]*128;side=1;cast=0;K=[0,0];st=[]
def F(fen):
 global side,cast
 b[:]=[0]*128;p=fen.split();s=112
 for ch in p[0]:
  if ch=='/':s-=24
  elif ch.isdigit():s+=int(ch)
  else:b[s]=" pnbrqk".index(ch.lower())*(2*(ch<'a')-1);s+=1
 side=2*(p[1]=='w')-1
 cast=sum(1<<i for i,c in enumerate("KQkq")if c in p[2])
 K[0]=b.index(6);K[1]=b.index(-6)
def A(s,by):
 for d in(15,17):
  t=s-d*by
  if not t&136 and b[t]==by:return 1
 for t in(2,6):
  for d in D[t]:
   x=s+d
   if not x&136 and b[x]==by*t:return 1
 for t in(3,4):
  for d in D[t]:
   x=s+d
   while not x&136:
    q=b[x]
    if q:
     if q==by*t or q==by*5:return 1
     break
    x+=d
 return 0
def g(co=0):
 ms=[]
 for s in G:
  p=b[s]
  if p*side<1:continue
  t=abs(p)
  if t==1:
   d=16*side
   for x in(s+d,s+d-1,s+d+1):
    if x&136:continue
    q=b[x];fw=x==s+d
    if fw:
     if q or co:continue
    elif q*d>=0:continue
    for r in((2,3,4,5)if(x>>4)==7*(d>0)else(0,)):ms.append(s|(x<<7)|(r<<14))
    if fw and(s>>4)==1+5*(d<0)and not b[s+2*d]and not co:ms.append(s|((s+2*d)<<7))
  else:
   for d in D[t]:
    x=s+d
    while not x&136:
     q=b[x]
     if q*side<0 or not q and not co:ms.append(s|(x<<7))
     if q or t in(2,6):break
     x+=d
   if t==6 and s==4+112*(side<0):
    rb=1+3*(side<0)
    for y in(1,-1):
     if cast&rb*(1+(y<0))and not(b[s+y]or b[s+2*y]or(y<0 and b[s+3*y]))and b[s+3*y-(y<0)]==side*4 and all(not A(s+i*y,-side)for i in(0,1,2)):ms.append(s|((s+2*y)<<7))
 return ms
def m(mv):
 global side,cast
 f=mv&127;t=(mv>>7)&127;pr=mv>>14;p=b[f];cap=b[t]
 st.append((mv,cap,cast));cast&=W.get(f,15)&W.get(t,15)
 n=pr*side if pr else p;b[t]=n;b[f]=0
 if abs(p)==6:
  K[side<0]=t
  if abs(t-f)==2:
   rf,rt=(t+1,t-1)if t>f else(t-2,t+1);b[rt]=b[rf];b[rf]=0
 side=-side
def u():
 global side,cast
 mv,cap,cast=st.pop();side=-side;f=mv&127;t=(mv>>7)&127;pr=mv>>14
 b[f]=side if pr else b[t];b[t]=cap
 if abs(b[f])==6:
  K[side<0]=f
  if abs(t-f)==2:
   rf,rt=(t+1,t-1)if t>f else(t-2,t+1);b[rf]=b[rt];b[rt]=0
def e():
 sc=0;n=0;Q=[0,0]
 for s in G:
  p=b[s]
  if not p:continue
  t=abs(p);q=(s&7)+8*(s>>4)^(56*(p<0))
  if t==6:Q[p<0]=q;continue
  v=V[t]+P[t][q]
  n+=V[t]*(t>1)
  sc+=v*(p>0 or-1)
 k=2 if n<1600 else 6
 sc+=P[k][Q[0]]-P[k][Q[1]]
 return sc if side>0 else-sc
def o(ms):
 return sorted(ms,key=lambda mv:V[abs(b[mv&127])]-10*V[abs(b[(mv>>7)&127])])
def S(d,al,be,ply=0):
 global nd,ab
 nd+=1
 if nd>=lim:ab=1;return 0
 ck=A(K[side<0],-side);best=-M
 if d<=0 and not ck:
  v=e()
  if v>=be:return v
  best=v
  if v>al:al=v
 for mv in o(g(d<=0 and not ck)):
  m(mv)
  if A(K[side>0],side):u();continue
  sc=-S(d-1+ck,-be,-al,ply+1);u()
  if ab:return 0
  if sc>best:best=sc
  if sc>al:
   al=sc
   if al>=be:return al
 if best==-M:return-M+ply if ck else 0
 return best
def r(nb):
 global nd,lim,ab
 lim=nb;nd=0;ab=0;bm=0;bs=-M;ms=[]
 for mv in g():
  m(mv)
  if not A(K[side>0],side):ms.append(mv)
  u()
 if not ms:return 0,0
 for d in range(1,13):
  ab=0;cb=ms[0];cs=-M;al=-M
  for mv in ms:
   m(mv);sc=-S(d-1,-M,-al,1);u()
   if ab:break
   if sc>cs:cs=sc;cb=mv
   if sc>al:al=sc
  if ab:break
  bm,bs=cb,cs
  ms.remove(bm);ms.insert(0,bm)
  if bs>M-100:break
 return bm,bs
def w(mv):
 x=""
 for s in(mv&127,(mv>>7)&127):x+=chr(97+(s&7))+str((s>>4)+1)
 pr=mv>>14
 if pr:x+="nbrq"[pr-2]
 return x
def p(u,da={}):
 return json.load(U.urlopen(u,json.dumps(da).encode()))
def main():
 url=os.getenv('MAKEFUN_ENV_URL')
 while 1:
  gg=p(url+'/game')
  if gg['status']=='done':break
  while gg['status']=='your_move':
   F(gg['fen']);mv,_=r(150000);z=gg['legal_moves'];x=w(mv)if mv and w(mv)in z else z[0]
   gg=p(url+'/move',{'game':gg['game'],'move':x})
main()
