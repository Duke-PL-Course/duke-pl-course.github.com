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

<!-- TODO: THE SLIDES BELOW -->

---

title: Maps

---

title: Functions

---

title: Binding and Destructuring

---

title: Using Higher-order Functions
class: segue dark

---

title: Anonymous Functions

---

title: Higher-order Functions

---

title: Recursion
class: segue dark

---
<!-- TODO -->
---

title: Working with Sequences
class: segue dark

---
<!-- TODO -->
---

title: Lazy Evaluation and Infinite Sequences
class: segue dark

---
<!-- TODO -->
---

title: Abstractions: Datatypes and Protocols
class: segue dark

---
<!-- TODO -->
---

title: Macros
class: segue dark
