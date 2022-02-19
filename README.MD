# OMNI HASHING ALGORITHM
## HOW IT WORKS
We convert a string to byte array, get size of the byte array if array is smaller then 32 bytes we do for loop to copy bytes from the start of the array and add size to it. If its more then 32 bytes we just delite everything after 32 bytes.
And at the end string is rotated by first by array size.
## Example
### hash of Hello World
```
0576f726c64537077777a2b627a7d776f537077777a2b627a7d776f5e7b828285366d8588827a5370777748656c6c6f2
```
### hash of Hello World1
```
576f726c6431547178787b2c637b7e78703d547178787b2c637b7e78703d607d848487386f878a847c4948656c6c6f20
```
### hash of Hello World123
```
f726c643132335457747b7b7e2f667e817b734041426357747b7b7e2f667e817b734041426366838a48656c6c6f20576
```
### As we see its not TOTALY difrent but small project to hash small strings