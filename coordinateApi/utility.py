


# Calculates distance between the given points and return 
def dist(a,b): return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.5

# This function takes in a list of points in form of  for example [(1,2),(2,4),(5,7),(8,12),(34,23),(67,8)]
#Finds closets pair of points.
#Param :  list of point e.g [(1,2),(2,4),(5,7),(8,12),(34,23),(67,8)]
#Return : two  close pair points  e.g ((1,2),(2,4))
def nearestpairpoints(points):
    minP1,minP2  = points[:2]
    minDist      = dist(minP1,minP2)
    base         = tuple(map(min,zip(*points)))
    sPoints      = sorted((dist(base,p),p) for p in points)
    iMin         = 0
    for ix,(xDist,px) in enumerate(sPoints[1:],1):
        for i,(iDist,pi) in enumerate(sPoints[iMin:ix],iMin):
            if iDist + minDist <= xDist: iMin = i+1; continue
            if dist(px,pi) >= minDist: continue
            minP1,minP2   = px,pi
            minDist       = dist(minP1,minP2)
    return minP1,minP2
    