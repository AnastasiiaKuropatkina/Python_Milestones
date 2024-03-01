# Milestone 3 “Pascal's Triangle”

Alice loves triangles and math. She wants to create a poster on the wall with [Pascal's triangle](https://en.wikipedia.org/wiki/Pascal%27s_triangle). Let's help her!

Create a file `triangle.py`, where define a function `def get_triangle(rows: int) -> List[List[int]]`, which will return the triangle as a list of lists with the specified number of rows:
```python
get_triangle(5) == 
[
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
]
```
In the same file, write logic to get the number of rows from command line arguments and print the resulting triangle to the console:
```python
python triangle.py 5
    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1
```