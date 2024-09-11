# Quaternions
Python library for processing quaternions and complex numbers

```python
from quaternions import Quaternion, pi

# equvivalent
quaternion = Quaternion(1, 2, 3, 4)
quaternion = Quaternion([1, 2, 3, 4])

print(quaternion)
# 1+2i+3j+4k

# equvivalent
quaternion = Quaternion(0, 1, 2, 3)
quaternion = Quaternion(1, 2, 3)

print(quaternion)
# 1i+2j+3k

print(Quaternion(1, 2, 3, 4)*Quaternion(4, 3, 2, 1))
# -12+6i+24j+12k

print(Quaternion(4, 3, 2, 1)*Quaternion(1, 2, 3, 4))
# -12+16i+4j+22k

# .rotate({base vector}, {angle (radians)})
# note: if angle is positive, then rotation is counter clockwise, and vice versa
print(Quaternion([0, 1, 0]).rotate([1, 0, 0], pi/2))
# 0i+0.0j+k
# note: if the program displays '0' it means that multiplier is exactly zero, but if the output is '0.0' it means that value was rounded to zero
# by default, values in displayed quaternions are rounded to three digets after point

# if you want the library to display multipliers precisely, specify it with 'precise' fucntion
print(Quaternion([0, 1, 0]).rotate([1, 0, 0], pi/2).precise())
# 0i+2.220446049250313e-16j+k
```
