subtitle: Haskell

---

title: Haskell Overview
build_lists: true

Haskell is ...

* A **purely** functional language with special emphasis on [lazy processing][]
* [strongly][] and [statically][] typed
* Allows Erlang-style pattern matching and guards, Clojure-style lazy evaluation, and list comprehensions from both Clojure and Erlang.
* Uses [monads][] to preserve state


[lazy processing]: http://en.wikipedia.org/wiki/Lazy_evaluation
[statically]: http://en.wikipedia.org/wiki/Static_typing#Static_typing
[strongly]: http://en.wikipedia.org/wiki/Strong_typing
[monads]: http://en.wikipedia.org/wiki/Monad_(functional_programming)

---

title: Getting Started

Run `ghci` to open Glasgow Haskell Compiler console.

use `:load file` to load source file

use `:reload` to reload source files

---

title: Expressions and Primitive Types
class: segue dark

---

title: Numbers

<script src="https://gist.github.com/5441163.js"></script>

---

title: Characters and Strings

`"this is a string"` and `'c'`is a character.

A string is just a list of characters.

Use `++` for string concatenation

<script src="https://gist.github.com/5441172.js"></script>

---

title: Boolean

Same as other languages, except for not equals, `/=`

---

title: Indentation

---

title: Type Inference

Use `:set +t` to turn on type annotations in the console, or use `:t exp` to see the type of an expression

<script src="https://gist.github.com/5441217.js"></script>

---

title: Functions
class: segue dark

---

title: Defining Functions in Console

A function declaration consists of 2 parts: an optional type specification and the implementation.

In the console, we will use `let` expressions to bind functions to the local scope.

<script src="https://gist.github.com/5441258.js"></script>

---

title: Defining Functions in Files

Notice that we added a module called Main. In Haskell, modules collect related code into a similar scope. The Main module is special. It is the top-level module.

<script src="https://gist.github.com/5441276.js"></script>

<script src="https://gist.github.com/5441308.js"></script>

---

title: Recursion

Going back to our beloved factorial function

<script src="https://gist.github.com/5441320.js"></script>

---

title: Recursion with Pattern Matching

<script src="https://gist.github.com/5441323.js"></script>

*Note*: the order of the patterns is important. Haskell will take matches in order.

---

title: Recursion with Guards

<script src="https://gist.github.com/5441339.js"></script>

---

title: Tuples and Lists
class: segue dark

---

title: Simple Fibonacci

<script src="https://gist.github.com/5441352.js"></script>

---

title: Fibonacci with Tuples

Tuples are in the form of `(item1, item2, etc...)` 

<script src="https://gist.github.com/5443813.js"></script>

---

title: Fibonacci with Pairs

<script src="https://gist.github.com/5443836.js"></script>

*Note*: `fst` takes the first element of a tuple
*Note*: `.` means function composition, or `f(g(x))`
*Note*: `fib = fst . fibNthPair` is equivalent to `fib n = fst (fibNthPair n)`

---

title: List Deconstruction

<script src="https://gist.github.com/5443908.js"></script>

Now use this to implement 2 functions:

* `prod list`, computes the product of all elements in a list
* `count list`, count the number of elements in a list

<script src="https://gist.github.com/5443987.js"></script>

---

title: List Construction

<script src="https://gist.github.com/5443956.js"></script>

Write a function called `allEven list`

<script src="https://gist.github.com/5443983.js"></script>

---

title: Ranges

<script src="https://gist.github.com/5443999.js"></script>

---

title: For Comprehensions

Very similar to Erlang's For Comprehensions

<script src="https://gist.github.com/5444013.js"></script>

---


title: Higher Order Functions
class: segue dark

---

title: Anonymous Functions

Anonymous functions are in the form of `(\param1 .. paramn -> function_body)`

<script src="https://gist.github.com/5444333.js"></script>

*Note*: `(+ 1)` is a partially applied function, and is equal to `(\x -> x + 1)`
*Note*: `+` is equal to `(\x y -> x + y)`

---

title: Partially Applied Functions and Currying

Every function in Haskell has one parameter, or is automatically [curried](http://en.wikipedia.org/wiki/Currying)

<script src="https://gist.github.com/5444381.js"></script>

When Haskell computes `prod 2 4`, it is really computing `(prod 2) 4`

1. apply `prod 2`. That returns the function `(\y -> 2 * y)`
2. apply `(\y->2*y) 4`, or `2*4`, giving you `8`

---

title: Lazy Evaluation

<script src="https://gist.github.com/5444427.js"></script>

<script src="https://gist.github.com/5444431.js"></script>

---

title: Conal Elliot - Functional Reactive Animation

[Link](http://conal.net/fran/tutorial.htm)

---

title: Classes and Types

---

title: User-Defined Types

---

title: Functions and Polymorphism

---

title: Recursive Types

---

title: Classes

---

title: Monad

---

title: Different Computational Strategies

---

title: Maybe Monad

---