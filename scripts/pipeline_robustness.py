"""Sensitivity diagnostics for correlated reductions of one eclipse."""
import numpy as np

def paired_offset(a, b, sigma_a, sigma_b, correlation=0.0):
    """Constant offset and formal SE for assumed same-bin correlation."""
    a,b,sa,sb=map(lambda x:np.asarray(x,dtype=float),(a,b,sigma_a,sigma_b))
    if a.ndim!=1 or a.size<2 or any(x.shape!=a.shape for x in (b,sa,sb)):
        raise ValueError("aligned one-dimensional arrays with >=2 bins required")
    if not all(np.all(np.isfinite(x)) for x in (a,b,sa,sb)) or np.any(sa<=0) or np.any(sb<=0) or not np.isfinite(correlation) or abs(correlation)>=1:
        raise ValueError("invalid measurements, errors or correlation")
    variance=sa**2+sb**2-2*correlation*sa*sb
    if np.any(variance<=0): raise ValueError("nonpositive variance")
    weights=1/variance
    return float(np.sum(weights*(a-b))/np.sum(weights)),float(np.sqrt(1/np.sum(weights)))

def delete_block_offsets(a,b,sa,sb,block_size,correlation=0.0):
    """Successive contiguous-bin deletions; not a bootstrap confidence interval."""
    n=len(a)
    if not isinstance(block_size,int) or block_size<1 or block_size>n-2:
        raise ValueError("block_size must leave at least two bins")
    results=[]
    for start in range(0,n,block_size):
        mask=np.ones(n,dtype=bool)
        mask[start:min(n,start+block_size)]=False
        if mask.sum()<2: continue
        results.append(paired_offset(*[np.asarray(x)[mask] for x in (a,b,sa,sb)],correlation))
    return np.asarray(results)
