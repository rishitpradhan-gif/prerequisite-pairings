# Exact legality of paired replies on prerequisite posets

Let P be a finite poset with an even number of elements and M a perfect matching. A legal claim takes a minimal unoccupied element. The initiator chooses a legal element x; the responder must immediately claim its mate. A matching is **universally legal** if no forced reply fails in any reachable sequence, ignoring terminal winning conditions.

For x let B(x) be its matching block and define

    D(x) = {B(z) : z < x and B(z) != B(x)}.

Strict predecessors here mean the transitive relation, not merely input cover edges.

## Theorem 1 — local characterization

M is universally legal if and only if D(a)=D(b) for every block {a,b}.

**Sufficiency.** At a completed-round position, each block is either entirely occupied or entirely unoccupied. If x is legal, all blocks in D(x) are occupied. The equality puts every external predecessor of its mate y in occupied blocks. The relation y<x is impossible because x was legal and y unoccupied. If x<y, claiming x supplies that internal predecessor. Thus y is legal. Induction over rounds proves the claim.

**Necessity.** Form the directed quotient graph Q with an edge A→B whenever a<b for elements in distinct blocks A,B. Universal legality permits a complete play: while vertices remain a minimal unoccupied vertex exists, and its reply is legal. Its block order respects every quotient edge. Consequently Q is acyclic.

Suppose a violating block exists; choose the earliest one B={x,y} in a topological order. Every earlier block has equal external predecessor sets at its endpoints. Orient its names so D(y)\D(x) is nonempty. The set I=D(x) is a quotient predecessor ideal: if R∈I and T→R, choose r∈R with r<x. Since R precedes B and its endpoint sets agree, a predecessor from T lies below r (regardless of which endpoint witnessed the edge). Transitivity gives T∈I. Iterating covers all ancestors.

Complete precisely I in topological order, claiming the lower endpoint first for a comparable block and either endpoint otherwise. Every external predecessor block is already occupied, so these rounds are legal. Now x is legal: its external predecessors lie in I, and y<x would imply D(y)⊆D(x), contrary to the choice. After claiming x, y is blocked by a predecessor in a block of D(y)\D(x). This contradicts universal legality. ∎

## Theorem 2 — quotient compression

For a universally legal matching, the reachable completed-round positions correspond bijectively to order ideals of Q. A complete response play consists of a linear extension of Q and one binary choice for each block whose endpoints are incomparable. Hence the number of complete plays is

    e(Q) · 2^t,

where e(Q) counts linear extensions and t counts incomparable matching blocks.

**Proof.** Any reachable occupied block set is predecessor closed by legality. Conversely any quotient ideal can be filled in a topological order, since its external predecessors occur earlier and an internal lower endpoint can be taken first. These observations give the bijection. A complete block ordering must respect Q; every such ordering is legal. Comparable endpoints force the initiator to choose the lower one, while incomparable endpoints allow either choice independently. ∎

## Algorithm and falsifiable scope

Compute transitive closure, label each predecessor by its matching block, remove the current block, and compare sets at mates. A direct implementation takes O(n³) time including closure; the set test is polynomial. Counting linear extensions is a separate counting problem: no efficient general counting algorithm is claimed.

The included verifier compares this local criterion against an independent explicit search of every reachable completed-round state. It covers every naturally labelled poset of sizes 2,4,6 and every perfect matching: 72,482 cases. Natural labelling loses no isomorphism type because every finite poset has a topological order. This finite test does not itself prove the unbounded theorem.

Winning conditions are intentionally absent. Universal legality is stronger than legality only along branches before a player's win. Adaptive rematching is outside the theorem.
