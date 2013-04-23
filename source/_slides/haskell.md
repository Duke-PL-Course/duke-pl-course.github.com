subtitle: Haskell

---

title: Haskell Overview
build_lists: true

Haskell is ...

* A **purely** functional language with special emphasis on [lazy processing][]
* [strongly][] and [statically][] typed
* Uses [monads][] to preserve state
* Supports a wide variety of functional capabilities including list comprehensions, lazy computing strategies, partially applied functions, and currying.


[lazy processing]: http://en.wikipedia.org/wiki/Lazy_evaluation
[statically]: http://en.wikipedia.org/wiki/Static_typing#Static_typing
[strongly]: http://en.wikipedia.org/wiki/Strong_typing
[monads]: http://en.wikipedia.org/wiki/Monad_(functional_programming)

---

title: Getting Started

Run `ghci` to open the interactive console

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

Boolean logic operations can be applied using infix operators or function calls

<script src="https://gist.github.com/5446318.js"></script>

---

title: Type Inference

Use `:set +t` to turn on type annotations in the console, or use `:t exp` to see the type of an expression

<script src="https://gist.github.com/5441217.js"></script>

---

title: Functions
class: segue dark

---

title: Defining Functions

A function declaration consists of 2 parts: an optional type specification and the implementation.

<script src="https://gist.github.com/5441276.js"></script>

<script src="https://gist.github.com/5441308.js"></script>

In the console, we will use `let` expressions to bind functions to the local scope.

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

title: Tuples

Tuples are in the form of `(item1, item2, etc...)` where items can be of different type

<script src="https://gist.github.com/5447078.js"></script>

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

<div id="hiddenfuncs" style="display: none;">
  <h4>Solution</h4>
  <br>
  <script src="https://gist.github.com/5443987.js"></script>
</div>

<script>$('body').keyup(function(e) { if (e.which == 83 /* 's' */ && slidedeck.curSlide_ == 15) {$('#hiddenfuncs').show('slow');} });</script>

---

title: List Construction

<script src="https://gist.github.com/5443956.js"></script>

Write a function called `allEven list`

<div id="hiddenalleven" style="display: none;">
  <h4>Solution</h4>
  <br>
  <script src="https://gist.github.com/5443983.js"></script>
</div>

<script>$('body').keyup(function(e) { if (e.which == 83 /* 's' */ && slidedeck.curSlide_ == 16) {$('#hiddenalleven').show('slow');} });</script>

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

* First, apply `prod 2`. That returns the function `(\y -> 2 * y)`
* Second, apply `(\y -> 2 * y) 4`, or `2 * 4`, giving you `8`

---

title: Lazy Evaluation

<script src="https://gist.github.com/5444427.js"></script>

<script src="https://gist.github.com/5444431.js"></script>

---

title: Conal Elliot - Functional Reactive Animation

[Link](http://conal.net/fran/tutorial.htm)

---

title: Types
class: segue dark

---

title: User-Defined Types

Use `data` to define custom types, and `type` to create aliases of existing types

<script src="https://gist.github.com/5446467.js"></script>

---

title: Recursive Types

<script src="https://gist.github.com/5446540.js"></script>

<script src="https://gist.github.com/5446543.js"></script>

---

title: Monads
class: segue dark

---

title: Monad

A *Monad* lets us compose functions in ways that have specific properties

A Monad has 3 components

* A type constructor that’s based on some type of container. The container could be a simple variable, a list, or anything that can hold a value

* A `return` function that wraps up a function and puts it in the container

* A bind function called `>>=` that unwraps a function. We’ll use bind to chain functions together.

---

title: Monad Rules

All monads will need to satisfy 3 rules. For some monad `m`, some function `f`, and some value `x`:

* You should be able to use a type constructor to create a monad that will work with some type that can hold a value.
* You should be able to unwrap and wrap values without loss of information.
    `(monad >>= return) == monad`
* Nesting bind functions should be the same as calling them sequentially.
    `((m >>= f) >>= g) == (m >>= (\x -> f x >>= g))`

---

title: Building a Monad from Scratch

*Note*: We’re using `>>==` and `rtn` instead of `>>=` and `return` to prevent collisions with Haskell’s built-in monad functions.

<script src="https://gist.github.com/5446765.js"></script>

---

title: Monads and do Notation

`do` notation creates syntactical sugar around monads

<script src="https://gist.github.com/5446829.js"></script>

* use `<-` for assignment
* Separate lines with `;`
* `let {expressions}`
* Wrap your code in `:{` and `}:` with each on a separate line

---

title: Maybe Monad

Haskell uses Maybe Monads to deal with potential failures

<script src="https://gist.github.com/5447170.js"></script>

<script src="https://gist.github.com/5447174.js"></script>

---

title: Wrapping 
class: segue dark

---

title: Strengths

* **Type System**
    Unobtrusive. Extremely flexible and robust with regard to working with custom types.
* **Expressiveness**
    Powerful syntax to express ideas very concisely
* **Purity of Programming Model**
    Purely functional nature means programs are more predictable and easier to reason about, particularly with complex concurrent applications
* **Lazy Semantics**
    Easier to build more concise programs that have better performance than mere recursion 
* **Academic Support**
    Strong research interest

---

title: Weaknesses

* **Inflexibility of Programming Model**
    Haskell makes some hard things easy, it also makes some easy things hard, such as sequential operations and io
* **Relatively Small Community**
* **Learning Curve**
    Monads and other parts of the language more intellectually demanding than many other languages
