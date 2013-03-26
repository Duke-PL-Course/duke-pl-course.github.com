subtitle: Erlang

---

title: Erlang Overview
build_lists: true

Erlang is ...

* Created by [Joe Armstrong][] at Ericsson
* A general-purpose [concurrent][], [garbage-collected][] programming language and runtime system
* A functional language, with [strict evaluation][], [single assignment][], and [dynamic typing][]
* Designed to support scalable, reliable, distributed, [fault-tolerant][], [soft-real-time][], non-stop applications
* Runs on the [BEAM Virtual Machine][]

[Joe Armstrong]: http://en.wikipedia.org/wiki/Joe_Armstrong_(programming)
[concurrent]: http://en.wikipedia.org/wiki/Concurrent_computing
[garbage-collected]: http://en.wikipedia.org/wiki/Garbage_collection_(computer_science)
[strict evaluation]: http://en.wikipedia.org/wiki/Strict_evaluation
[single assignment]: http://en.wikipedia.org/wiki/Single_assignment
[dynamic typing]: http://en.wikipedia.org/wiki/Dynamic_typing
[fault-tolerant]: http://en.wikipedia.org/wiki/Fault-tolerance
[soft-real-time]: http://en.wikipedia.org/wiki/Soft_real-time
[BEAM Virtual Machine]: http://www.erlang.org/doc/man/beam_lib.html

---

title: Code Example

<script src="https://gist.github.com/yangsu/5198282.js"></script>

---

title: Built for Concurrency

* No Threading
* Lightweight Processes
* Uses actors/message passing for concurrency, similar to Scala’s message passing syntax. 
    * In Scala, an actor represents an object, backed by a thread pool
    * In Erlang, an actor represents a lightweight process. The actor reads inbound messages from a queue and uses *pattern matching* to decide how to process it.
* *"Let it crash"* Erlang makes it easy to monitor, kill, and spawn processes. You can also hot-swap code, meaning you can replace pieces of your application without stopping your code

---

title: Who Uses Erlang?
build_lists: true

* **Amazon.com** uses Erlang to implement SimpleDB, providing database services as a part of the Amazon Web Services offering
* **Yahoo!** uses it in its social bookmarking service, Delicious, which has more than 5 million users and 150 million bookmarked URLs
* **Facebook** uses Erlang to power the backend of its chat service, handling more than 100 million active users
* **T-Mobile** uses Erlang in its SMS and authentication systems
* **Motorola** is using Erlang in call processing products in the public-safety industry
* **Ericsson** uses Erlang in its support nodes, used in GPRS and 3G mobile networks worldwide
* **Linden Lab** uses Erlang in its games

---

title: Functional Programming
build_lists: true

Erlang is the first of our functional languages. (Scala is a hybrid functional/object-oriented language.). To you this means:

* Your programs are going to be built entirely out of functions, with no objects anywhere.
* Those functions will *usually* return the same values, given the same inputs.
* Those functions will not *usually* have side effects, meaning they will not modify program state.
* You will only be able to assign any variable once.

---

title: Getting Started

Erlang files end with `.erl`

To start a Erlang shell, use the command `erl` in your terminal

To compile Erlang files, refer to the [slide on functions](#17)

---

title: Basic Syntax
class: segue dark

---

title: Expressions and Statements

The syntax is very similar to Prolog.

All statements end with a **period**

<script src="https://gist.github.com/5199078.js"></script>

Note:

* `2 + 2.0` => `4.0` means that Erlang does some basic type coercion  
* In Erlang, strings are just syntactical sugar for a *list* of integer ASCII code

---

title: Atoms and Variables

Like Prolog, **atoms** must begin with *lowercase letters* and **Variables** begin with *uppercase letters*

<script src="https://gist.github.com/5199206.js"></script>

---

title: Lists and Tuples

**Lists** are *heterogeneous* and can be *any* length

**Tuples** are *fixed-length* *heterogeneous* lists

<script src="https://gist.github.com/5199234.js"></script>

---

title: Pattern Matching

Again, very similar to Prolog's pattern matching.

In Ruby, hash maps are used to associate names with values. In Erlang, you’ll often see tuples used as you would use maps or hashes.

<script src="https://gist.github.com/5199355.js"></script>

---

title: List Pattern Matching

<script src="https://gist.github.com/5199447.js"></script>

Note: In Prolog, `=` means unification. In Erlang, `=` is a pattern match. This is a **key** difference

---

title: Bit Pattern Matching

Erlang also makes it very easy to pack and unpack bits

<script src="https://gist.github.com/5199457.js"></script>

---

title: More Bit Pattern Matching

<script src="https://gist.github.com/sudowork/5243717.js"></script>

---

title: Functions
class: segue dark

---

title: Workflow

You’re going to write functions in files with the `.erl` extension.

Each file contains code for a module, and you have to compile it to run it. The filename **must** match the module name.

After you’ve compiled a file, it produces a `.beam` executable. 

The `.beam` compiled module will run in a virtual machine called the `beam`.

---

title: Mirror Function

<script src="https://gist.github.com/5199533.js"></script>

To compile this file, use `c(filename).`. You don't have to include the `.erl` extension as part of the `filename`. Once compiled, you will find a `filename.beam` file in the same directory. 

<script src="https://gist.github.com/5199624.js"></script>

Note: You must scope the functions with their module names followed by a `:`

---

title: Translate Number Function

<script src="https://gist.github.com/5199665.js"></script>

The `number/1` function contains multiple pattern match possibilities. Each possible match has the *function name*, the *argument to match*, and the *code to execute* after the `->` symbol. Terminate the last statement with `.` and all others with `;`.

<script src="https://gist.github.com/5199722.js"></script>

---

title: Factorial and Fibonacci Function

<script src="https://gist.github.com/5199788.js"></script>

Like Prolog, Erlang is also optimized for tail recursion.

<script src="https://gist.github.com/5199784.js"></script>

---

title: Control Structures
class: segue dark

---

title: Case Expression

Given an expression, you can use the `case` control structure to select the appropriate resulting expression. This is particularly useful because you can take advantage of pattern matching.

<script src="https://gist.github.com/sudowork/5244080.js"></script>

---

title: If Expression

The `if` expression is used similarly to the `case` expression; however, instead of using pattern matching, [**guards**][guards] are used. Common *guard expressions* are as follows: the atom `true`, other terms, certain BIFs (see link), term comparisons, arithmetic expressions, boolean expressions, and short-circuit expressions (`andalso`, `orelse`). A full **guard** is a list of *guard expressions* separated by `,` (think of it as an **AND**). Guards can then be combined in sequence using `;` (**OR**) to form **guard sequences**.

Note that at least one of the branches must evaluate to `true`; otherwise, a runtime exception is thrown. It is idiomatic to have a `true -> ...` branch in order to represent `else`, which does not exist in erlang.

[guards]: http://www.erlang.org/doc/reference_manual/expressions.html#id80039

---

title: Using If Expressions

<script src="https://gist.github.com/sudowork/5244196.js"></script>

---
