#     --    -
#   --  -  - -
# --     --   -

# Example: [0, 0, 1, 1, 2, 2, 1, 0, 0, 1, 2, 1, 0] -> 6
# profile -> volume

# Note: it's possible for elevation to drop from 2 to 0.
# Elevations are always integers. Elevation is not larger than max integer.
# Beginning and end of topography is always 0

# What if we had a function called depth


#     --
#   --  -  --
# --     --  -
enumerate('abc') -> [(0, 'a'), (1, 'b'), (2, 'c')]


def depth(topo, i):
    # Depth = ((The minimum of the maximum height to your left and the
    # maximum height to your right) - Current elevation) ## only if this is
    # non-negative

    maxLeft = max(topo[0:i - 1])  # should be max_left
    maxRight = max(topo[i + 1:])

    waterline = min(maxLeft, maxRight)

    if (waterline - topo[i]) < 0:
        return 0
    else:
        return waterline - topo[i]


def volume(topo):
    # O(n**2)

    totalVolume = 0

    for i in range(len(topo)):

        totalVolume += depth(topo, i)

    return totalVolume
