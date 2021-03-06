subtitle: Clojure

---

title: Clojure Overview
build_lists: true

Clojure is ...

* A modern [Lisp][] dialect
* Created by [Rich Hickey][] in 2007
* A functional language, with [immutable values][], [strong typing][], [dynamic typing][], and [software transactional memory][]
* Augmented with a powerful [macro system][]
* Made to run on the [Java Virtual Machine][]
* Tightly integraded with [Java][] applications

[Java Virtual Machine]: http://en.wikipedia.org/wiki/Jvm
[Java]: http://en.wikipedia.org/wiki/Java_(programming_language)
[Lisp]: http://en.wikipedia.org/wiki/Lisp_(programming_language)
[Rich Hickey]: https://github.com/richhickey
[dynamic typing]: http://en.wikipedia.org/wiki/Dynamic_typing
[immutable values]: http://en.wikipedia.org/wiki/Immutable_object
[macro system]: http://clojure.org/macros
[software transactional memory]: http://en.wikipedia.org/wiki/Software_transactional_memory
[strong typing]: http://en.wikipedia.org/wiki/Strong_typing

---

title: Code Example

<script src="https://gist.github.com/sudowork/5283585.js"></script>

---

title: Installing Leiningen

[Leiningen][] is a simple build tool used for automatic Clojure projects.

To install on OS X (with brew + bash):

<script src="https://gist.github.com/sudowork/5283665.js"></script>

To install on the VM running Lubuntu:

<script src="https://gist.github.com/sudowork/5283669.js"></script>

[Leiningen]: https://github.com/technomancy/leiningen

---

title: Creating a New Clojure Project

We are going to create a new project/workspace to use for our code. It's going to make things easier, and we're also going to use the Leiningen **REPL**.

<script src="https://gist.github.com/sudowork/5283709.js"></script>

---

title: Functions and Basic Data Types
class: segue dark

---

title: Forms

A **form** in Clojure is the basic building block for a Clojure program. A program can simply be thought of as a sequence of forms (and macros). Examples of forms include: function calls, booleans, characters, numbers, keywords, and strings.

There also exist built-in [special forms][] that perform core operations.

[special forms]: http://clojure.org/special_forms

---

title: Calling Basic Functions

Clojure using **prefix notation** for calling functions/operators. There is no native way to use **infix notation**.

<script src="https://gist.github.com/sudowork/5283741.js"></script>

---

title: Multiple Parameter Lists

Functions in clojure can be defined to accept varying-length parameter lists (**arity**). We already saw an example of this using the `-` function.

Behavior can vary based on the number of parameters passed to the function.

<script src="https://gist.github.com/sudowork/5283761.js"></script>

---

title: Type Coercion

Just like Ruby, the Clojure compiler will try to coerce types at runtime. Remember, Clojure is dynamically typed.

Failure to perform a coercion will result in a [ClassCastException][], which is a runtime exception from the Java class hierarchy.

<script src="https://gist.github.com/sudowork/5283924.js"></script>

[ClassCastException]: http://docs.oracle.com/javase/1.5.0/docs/api/java/lang/ClassCastException.html

---

title: Strings and Chars

<script src="https://gist.github.com/sudowork/5283972.js"></script>

---

title: Booleans and Conditional Expressions

<script src="https://gist.github.com/sudowork/5283985.js"></script>

---

title: Core Data Structures: Lists, Maps, Sets, and Vectors
class: segue dark

---

title: Lists

[Lists][] are one of the core data structures to Clojure and all dialects of Lisp. In fact, Lisp stands for **lis**t **p**rocessing.

It is a **sequential** data structure that does not allow for random access.

<script src="https://gist.github.com/sudowork/5284130.js"></script>

[Lists]: http://clojure.org/data_structures#Data%20Structures-Lists%20(IPersistentList)

---

title: Vectors

[Vectors][] are similar to lists; however, they are **indexable**, meaning you can randomly access elements in the vector.

To access an element of a vector, you can either call the `nth` function or directly use the vector as a function that takes an index as the argument.

<script src="https://gist.github.com/sudowork/5284224.js"></script>

[Vectors]: http://clojure.org/data_structures#Data%20Structures-Vectors%20(IPersistentVector)

---

title: Sets

**Sets** are unordered collections of unique elements.

<script src="https://gist.github.com/sudowork/5284381.js"></script>

---

title: Maps

**Maps** are associative data structures that associate a key to a value.

For readability, Clojure introduces commas as whitespace in addition to conventional Lisp syntax.

<script src="https://gist.github.com/sudowork/5293377.js"></script>

---

title: Functions
class: segue dark

---

title: Functions

Use the `defn` macro to define new functions `defn name doc [params] body`

<script src="https://gist.github.com/sudowork/5293462.js"></script>

*Note*: We haven't talked about macros yet, but basically, `defn` will call `def` and associate a **Var** in the current namespace with an anonymous function. Essentially, creating a new function in the current namespace.

*Note*: You can used `doc` on any function that specifies a documentation line

---

title: Multiple-arity Functions

Remember the functions that accept varying length parameter lists? Let's learn how to make one of those. To clarify, the number of parameters a function accepts denotes its **arity**.

We also introduce [`apply`][apply] here to reflectively call a function with a list of parameters. This example is naive, and unidiomatic. We will discuss better techniques later on.

<script src="https://gist.github.com/sudowork/5293626.js"></script>

[apply]: http://richhickey.github.com/clojure/clojure.core-api.html#clojure.core/apply

---

title: Binding and Destructuring

When a function is called with parameters, the parameters are **bound** to function's scope with a given name.

In other words `(defn id [x] x), (id 42)` binds the value `42` to the alias `x` in the function's scope. `x` would be unavailable to be used outside of the function.

Clojure let's you use bind aliases within arguments. This process is called **destructuring**, and it is part of *pattern matching*. The difference is that pattern matching is *conditional*; whereas, destructuring is simply pulling apart a value.

<script src="https://gist.github.com/sudowork/5294320.js"></script>

---

title: More Destructuring and Local Bindings

<script src="https://gist.github.com/5398407.js"></script>

---

title: Destructuring Using Let Statements

`let` takes 2 arguments: a **vector** with symbol(s) you want to bind followed by the value you want bound, and an **expression** that uses the bound values

<script src="https://gist.github.com/5398437.js"></script>

---

title: Using Higher-order Functions
class: segue dark

---

title: Anonymous Functions

Clojure also allows for anonymous functions using form `(fn [parameters*] body)`. In fact, the `defn` macro just expands into a `def` using an `fn`.

<script src="https://gist.github.com/5398538.js"></script>

Or use *reader macro* `#(expression with %)`, which binds `%` to each item in a sequence of parameters.

<script src="https://gist.github.com/5398552.js"></script>

---

title: Higher-order Functions

Of course, anonymous functions themselves aren't too useful. Let's combine them with some higher order functions.

<script src="https://gist.github.com/sudowork/5393840.js"></script>

---

title: Implement Fibonacci

<script src="https://gist.github.com/yangsu/5398809.js"></script>
<script src="https://gist.github.com/yangsu/5398907.js"></script>

---

title: Implement Factorial

<script src="https://gist.github.com/5399832.js"></script>
<script src="https://gist.github.com/5399874.js"></script>
<script src="https://gist.github.com/5399900.js"></script>

---

title: Recursion
class: segue dark

---

title: Tail Call Optimization in Clojure

Typically, functional languages use **recursion** in place of loops. This leads to the dreaded **stack overflow** problem as we recurse deeper.

Fortunately, most functional languages provide either automatic [**tail call optimization**][tco] (TCO).

Unfortunately, Clojure does not support automatic TCO because the JVM does not natively support TCO.

*Side note: Scala is able to do automatic TCO because the Scala compiler does the translation into loops*.

To get around this, we can explicitly perform the TCO ourselves using the `recur` and `loop` special forms.

`(loop [x initial-x, y initial-y] (do-something-with x y))`

Out of the scope of this class, you can also use the [`trampoline`][trampoline] technique to optimize mutually recursive functions.

[tco]: http://en.wikipedia.org/wiki/Tail_call
[tramposine]: http://pramode.net/clojure/2010/05/08/clojure-trampoline/

---

title: Recur and loop example

<script src="https://gist.github.com/sudowork/5394099.js"></script>

---

title: Sequences
class: segue dark

---

title: What is a Sequence?

A [Sequence][] in clojure is just a wrapper interface (`ISeq`) for collections (vectors, lists, etc.).

There exists a library of functions just for acting on sequences, which means that we can treat sequences pretty generically.

[Sequence]: http://clojure.org/sequences

---

title: List Comprehensions on Sequences

Similar to Scala, Clojure has for/list comprehensions, that work to combine `map`, `filter`, and the concept of permutations.

Binding in a for comprehension syntactically looks the same as the `let` or `loop` special forms.

<script src="https://gist.github.com/sudowork/5394282.js"></script>

---

title: Lazy Evaluation and Infinite Sequences
class: segue dark

---

title: Finite Sequences with range

Like Ruby, Clojure supports ranges as functions

<script src="https://gist.github.com/5399172.js"></script>

---

title: Infinite Sequences and take

`(repeat element)` creates an infinite sequence of copies of `element`

`(cycle list)` creates an infinites sequence by cycling elements in a list

`(take n infinite-sequence)` takes the first `n` elements of an infinite sequence

`(drop n infinite-sequence)` drops the first `n` elements of an infinite sequence

Use `->>` to apply functions left to right rather than using prefix notation

<script src="https://gist.github.com/5399232.js"></script>

---

title: More Infinite Sequence Operations

`(interpose element seq)` inserts `element` between every pair of elements in `seq`

`(interleave seq1 seq2)` interleaves the elements of the 2 sequences

`(iterate fn init)` creates a sequence by applying `fn` to `init` and the successive return values

<script src="https://gist.github.com/5399298.js"></script>

---

title: Fibonacci using Infinite Sequences
build_lists: true

* Iterator function to describe each step of Fibonacci  
  `(defn fib-pair [[a b]]  [b (+ a b)])`
* Generate an infinite sequence of Fibonacci pairs  
  `(iterate fib-pair [1 1])`
* Extract the first element of the sequence of pairs to construct the infinite Fibonacci sequence  
  `(map first (iterate fib-pair [1 1]))`
* Using take to compute the first 5 elements of the Fibonacci Sequence  
  `(take 5 (map first (iterate fib-pair [1 1])))`
* Using `nth` to compute the 50th Fibonacci number  
  `(nth (map first (iterate fib-pair [1 1])) 50)`

---

title: Factorial using Infinite Sequences
build_lists: true

* Generate an infinite sequence  
  `(iterate inc 1)`
* Using `take` to get the sequence `1..N`  
  `(take n (iterate inc 1))`
* Using `apply` and the operator `*` to compute the product of `1..N`  
  `(apply * (take n (iterate inc 1)))`
* Define a function `factorial` to return the result  
  `(defn factorial [n] (apply * (take n (iterate inc 1))))`

---

title: Abstractions: Datatypes and Protocols
class: segue dark

---

title: Macros
class: segue dark

A Clojure program executes in two stages. Macro expansion translates all macros in the language to their expanded form. You can see what’s happen- ing with a command called `macroexpand`

<script src="https://gist.github.com/5400017.js"></script>
