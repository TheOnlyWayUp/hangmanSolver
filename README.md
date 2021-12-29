HangmanSolver
---------------------------
Async-Friendly Hangman solver.

Source - https://github.com/TheOnlyWayUp/hangmanSolver

Wiki - https://github.com/TheOnlyWayUp/hangmanSolver/wiki


Examples
----------------
```python
    import hangman, asyncio
    h = hangman.HangmanSolver()
    solve = asyncio.run(h.solve("Ca_e"))
    print(f"{solve.len} possible answers for {solve.query}.\n{solve.words}.\n\nDir - {dir(solve)}")
```
Output - 
```
22 possible answers for Ca_e.
['Cade', 'Cade', 'Cafe', 'Cafe', 'Cage', 'Cage', 'Cake', 'Cake', 'Came', 'Came', 'Cane', 'Cane', 'Cape', 'Cape', 'Care', 'Care', 'Case', 'Case', 'Cate', 'Cate', 'Cave', 'Cave'].

Dir - ['__annotations__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'len', 'query', 'words']
```
Interactive -

```python
    import hangman, asyncio
    h = hangman.HangmanSolver(interactive=True)
    solve = asyncio.run(h.solve())
    print(f"{solve.len} possible answers for {solve.query}.\n{solve.words}.\n\nDir - {dir(solve)}")
```
Output -
```
> Enter all known values as letters, and unknown values as _s.
> Example - If the word to guess is 'Cake', and only the letter 'e' is given, you should enter '___e'.

Ca_e

22 possible answers for Ca_e.
['Cade', 'Cade', 'Cafe', 'Cafe', 'Cage', 'Cage', 'Cake', 'Cake', 'Came', 'Came', 'Cane', 'Cane', 'Cape', 'Cape', 'Care', 'Care', 'Case', 'Case', 'Cate', 'Cate', 'Cave', 'Cave'].

Dir - ['__annotations__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'len', 'query', 'words']
```

Created by TheOnlyWayUp#1231 - https://github.com/TheOnlyWayUp/
