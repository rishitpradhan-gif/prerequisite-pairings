from functools import lru_cache
from itertools import combinations
import time,json

def matchings(xs):
 if not xs:yield ();return
 for j in range(1,len(xs)):
  for rest in matchings(xs[1:j]+xs[j+1:]):yield ((xs[0],xs[j]),)+rest

def poses(n):
 edges=list(combinations(range(n),2));seen=set()
 for mask in range(1<<len(edges)):
  p=[0]*n
  for j,(a,b) in enumerate(edges):
   if mask>>j&1:p[b]|=1<<a
  for b in range(n):
   for a in range(b):
    if p[b]>>a&1:p[b]|=p[a]
  t=tuple(p)
  if t not in seen:seen.add(t);yield t

def brute(p,mat):
 n=len(p);mate={x:y for a,b in mat for x,y in [(a,b),(b,a)]};todo=[0];seen={0}
 while todo:
  state=todo.pop()
  for x in range(n):
   if state>>x&1 or p[x]&~state:continue
   after=state|1<<x;y=mate[x]
   if p[y]&~after:return False
   after|=1<<y
   if after not in seen:seen.add(after);todo.append(after)
 return True

def local(p,mat):
 ids={x:j for j,ab in enumerate(mat) for x in ab}
 def d(x):return {ids[y] for y in range(len(p)) if p[x]>>y&1 and ids[y]!=ids[x]}
 return all(d(a)==d(b) for a,b in mat)

def check_quotient(p,mat):
 from functools import lru_cache
 n=len(p); m=len(mat); ids={x:j for j,ab in enumerate(mat) for x in ab}
 pred=[0]*m
 for x in range(n):
  for y in range(n):
   if p[x]>>y&1 and ids[x]!=ids[y]:pred[ids[x]]|=1<<ids[y]
 ideals=[s for s in range(1<<m) if all(not(s>>j&1) or not(pred[j]&~s) for j in range(m))]
 @lru_cache(None)
 def extensions(s):
  if s==(1<<m)-1:return 1
  return sum(extensions(s|1<<j) for j in range(m) if not(s>>j&1) and not(pred[j]&~s))
 mate={x:y for a,b in mat for x,y in ((a,b),(b,a))}; reached=set()
 @lru_cache(None)
 def plays(s):
  reached.add(s)
  if s==(1<<n)-1:return 1
  total=0
  for x in range(n):
   if s>>x&1 or p[x]&~s:continue
   y=mate[x];after=s|1<<x
   assert not(p[y]&~after)
   total+=plays(after|1<<y)
  return total
 actual=plays(0)
 expected_states={sum((1<<a)|(1<<b) for j,(a,b) in enumerate(mat) if s>>j&1) for s in ideals}
 assert reached==expected_states
 t=sum(not(p[a]>>b&1) and not(p[b]>>a&1) for a,b in mat)
 assert actual==extensions(0)*(1<<t)

def verify():
 results=[]
 for n in (2,4,6):
  count=good=0
  for p in poses(n):
   for mat in matchings(tuple(range(n))):
    a=local(p,mat); b=brute(p,mat)
    assert a==b, (p,mat)
    count+=1;good+=a
    if a:check_quotient(p,mat)
  results.append(dict(vertices=n,cases=count,universally_legal=good))
 return dict(status="passed",quotient_state_and_play_counts="checked on every universally legal instance",exhaustive=results,total_cases=sum(r["cases"] for r in results),scope="All naturally labelled posets on 2,4,6 vertices and all perfect matchings; every finite poset admits a natural labelling.")
if __name__=="__main__":
 result=verify()
 print(json.dumps(result,indent=2))
