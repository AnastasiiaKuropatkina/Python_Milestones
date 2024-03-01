# Milestone 1 “Back to school”

Alice and Bob love maths! They are now studying quadratic equations. They noticed that it didn’t make sense to blindly apply the formula every time and decided to automate this process. Could you help them?

Your task is to write a solver for quadratic equations. The user enters an equation as a string of the form: `<a>x^2 + <b>x + <c> = 0`

This may seem like a lot, so this time let's decompose the problem to several manageable steps.

> [!IMPORTANT]
> You may not use `if`-statements in this milestone. It is possible to accomplish all the steps using the functions that we've covered this week.

## Step 1. Process input

A user replaces letters with actual numbers, either positive or negative, for example:
```python
5x^2 + (-5)x + (-10) = 0
```
But a user can accidentally put an extra space or omit a space, for example:
```python
5x^2 +4x +    (-10) =  0
```
Let's start by extracting `a`, `b`, and `c` from user input and storing it to variables.
```python
eq = '4x^2 +4x +    (-8) =  0'

a = int(eq.replace(...)...)
b = ...
c = ...

print(a, b, c) # 4 4 -8
```
## Step 2. Calculate answer
Now, once we have all the coefficients, let's remind ourselves of the quadratic formula:

!['The quadratic formula'](./1705016957171_image.png "The quadratic formula")

Let's find `x1` and `x2!`
```python
x1 = ...
x2 = ...

print(x1, x2) # 1 -2
```