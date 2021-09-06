# Cluster (Big)

# Q
- Given a large number of edges whose distance is described as 24 bits, compute the largest value of k such that there is a k-clustering with spacing at least 3. This means how many clusters are needed to ensure all edges in a cluster are at most 2 bits different

# A
- Create a list of integers from input bits
- Create a map whose key is an integer from the list and value is an array of indexes of the list (make sure edge distances are not distinct)
- Initialize an Union-Find instance with the number of nodes
- Create a list of bit masks for distances (0 ~ 2)
  - Make sure to create a bit mask for 0-bit distance since there are edges with same distance
  - The # of variations of 24 bit masks with the 1-bit distance should be 24 (24C1)
  - The # of variations of 24 bit masks with the 2-bit distance should be 276 (24C2)
  - Make sure there are 301 bit masks in total
- Iterate all keys in the map in outer loop and iterate all bit masks inside
- Iff the key XOR a bit mask (call it neighbor) is in keys in the map, union all indexes stored in the key and the neighbor
- Count distinct root in the Union-Find
