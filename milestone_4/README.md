# Milestone 4 “Trade-offs”

Alice and Bob are playing the game: they have a random list of numbers and whoever first finds the pair of numbers such that they add up to a pre-agreed number - wins.

Carol sees their game and wants to win it, but Alice is unbeatable, she finds the pairs very quickly. So instead, he decided to use a program to play this game with her.

Let's write the function `find_sum(target: int, li: List[int]) -> Tuple[int, int]`. It should find the pair of elements in `li` that sum up to the `target`` value. You can assume the answer always exists, and if there are multiple answers - return any.

```python
assert find_sum(5, [1, 2, 3, 4 5]) in {(0, 3), (1, 2)}
```

First, let's approach this problem in a brute-force manner. Just iterate over all of the pairs with a double for-loop. Write the comment in the code with the time and space complexity of your algorithm.

Then, we can utilize a common pattern in solving algo problems - trading space for time! That means that our program can additionally utilize a more convenient data structure to improve time complexity.

Write function `find_sum_fast(target: int, li: List[int]) -> Tuple[int, int]`, which will do the same as find_sum, but with lower time complexity. Write the comment in the code with the time and space complexity of the new algorithm.