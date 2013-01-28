subtitle: Ruby

---

title: Ruby Overview
build_lists: true

Ruby is ...

* Created by Yukihiro (Matz) Matsumoto
* [Interpreted][]: No compilation necessary, code is executed by an interpreter
* [Object-oriented][]: Everything is an object
* [Strongly typed][]: Types must be compatible or <em>coercible</em>
* [Dynamically typed][]: Type checking is performed at run-time
* [Duck typed][]: more on this later
* Commonly used for scripting and web development (Rails)

[Interpreted]: http://en.wikipedia.org/wiki/Interpreted_language
[Object-oriented]: http://en.wikipedia.org/wiki/Object-oriented_programming
[Strongly typed]: http://en.wikipedia.org/wiki/Strong_typing
[Dynamically typed]: http://en.wikipedia.org/wiki/Type_system#Dynamic_typing
[Duck typed]: http://en.wikipedia.org/wiki/Duck_typing

---

title: Code Example

<script src="https://gist.github.com/4652670.js"></script>

---

title: Purely Object Oriented

_Everything_ in Ruby is an object

<script src="https://gist.github.com/4652698.js"></script>

---

title: Typing

In addition to being object-oriented, Ruby is **strongly** and **dynamically** typed

<script src="https://gist.github.com/4652806.js"></script>

---

title: Duck Typing

The duck test:

<blockquote>
  "If it looks like a duck, swims like a duck, and quacks like a duck, then it probably is a duck."
</blockquote>

<br>

Ruby is duck-typed, meaning that if two objects of different classes have the same method signature, then they can be used together.

<script src="https://gist.github.com/4652821.js"></script>

---

title: Variables

<script src="https://gist.github.com/4652825.js"></script>

---

title: Ranges

* inclusive `1..3`
* exclusive `1...3`

---

title: Functions

<script src="https://gist.github.com/4652826.js"></script>

We saw a bit of defining a function earlier in add_stuff

Notice that you didn't need to specify parameter types, return types, or even a return statement

**Every function returns something**. If you do not specify an explicit return, the function will return the value of the last expression that’s processed before exiting.

<script src="https://gist.github.com/4652828.js"></script>

---

title: Operators

[Full table of operators](http://www.techotopia.com/index.php/Ruby_Operator_Precedence#Operator_Precedence_Table)

#### Comparison operators (order of precedence):
* `( )`   Note: not really an operator
* `<=`, `<`, `>`, `>=`
* `<=>`, `==`, `===`, `!=`, `=~`, `!~`

#### Logical Operators
* Short circuit: `&&`, `and` Whole expression: `&`
* Short circuit: `||`, `or` Whole expression: `|`
* `not`, `!`

---

title: Tricky Precedence Nuance

* Don't use `or`, `and`, or `not` when dealing with assignment, and don't mix `&&` and `||` with `and` and `or`.
* Why? `and`, `or`, and `not` are lower precedence than assignment.
* So when is it okay to use them?

Why not use them?

<script src="https://gist.github.com/4652831.js"></script>

---

title: Control Structures

### Expression modifiers
`if`, `unless`, `while`, `until`

### Falsy Values
everything but `nil` and `false` evaluate to true. `0` is true!

---

title: Arrays

Arrays in Ruby can contain mixed types

<script src="https://gist.github.com/4652835.js"></script>

---

title: More Arrays

`[]` and `[]=` are just methods of the Array class; their typical usage is just syntactic sugar

Multidimensional arrays are just arrays of arrays

`push`, `pop`, as well as other functions exist natively in the [Array API][Array] that allow arrays to be used as queues, linked lists, stacks, or sets.

[Array]: http://www.ruby-doc.org/core-1.9.3/Array.html

---

title: Hashes/maps

<script src="https://gist.github.com/4652840.js"></script>

**symbol**s are identifying values/objects. Two symbols of the same name always refer to the same object id

---

title: Named Parameters

Hashes can be used to implement Named Parameters

<script src="https://gist.github.com/4652844.js"></script>

---

title: Code Blocks

`{ ... }` code between braces is a code block; alternatively, `do ... end` (usually for multi-line blocks) syntax can be used

`Fixnum.times` can be used to loop a certain number of times: `3.times { puts 'Hello, World!' }`

Use `each` on a collection (Array or Hash) to iterate over the elements in the collection: `animals.each { |a| puts a }` and `numbers.each { |k,v| puts "#{k} maps to #{v}" }`

---

title: Yielding

Augmenting a class definition and using **yield** to call a block

<script src="https://gist.github.com/4652848.js"></script>

---

title: Call

Alternatively, call a block using `call`. When we do this, the block is actually an instance of [`Proc`][Proc] (short for procedure). The main difference is that a [`Proc`][Proc] can be stored.

Useful for policy enforcement, conditional execution, transactions, etc.

[Proc]: http://www.ruby-doc.org/core-1.9.3/Proc.html

---

title: Code For Call
content_class: small

<script src="https://gist.github.com/4652852.js"></script>

---

title: Block Example - Tree Implementation

[Source](https://github.com/Duke-PL-Course/Ruby/blob/master/examples/2013-01-22-lecture02.rb#L71-L120)

---

title: Classes

**Conventions**

* Classes start with **capital letters** and typically use `CamelCase` to denote capitalization

* **Instance variables** and **method names** begin with **lowercase letters** in the `underscore_style`. Constants are in `ALL_CAPS`

* Functions and methods that test (return a boolean value) typically use a question mark (`if test?`)

* A **constructor** can be defined by overwriting the `initialize` method

---

title: Methods And Method Encapsulation

<script src="https://gist.github.com/4652856.js"></script>

---

title: Methods And Method Encapsulation

Or Alternatively

<script src="https://gist.github.com/4652861.js"></script>

---

title: Variables

Several ways to declare instance variables

* direct use/undeclared
* `attr` defines an instance variable and a method to access it
* `attr_reader` defines an instance variable, an accessor
* `attr_writer` defines an instance variable, and a setter
* `attr_accessor` defines an instance variable, an accessor, and a setter

---

title: Instance Variables


<script src="https://gist.github.com/4652864.js"></script>

To access the variables, you must prepend **instance variables** (one value per object) with `@` and class variables (one value per class) with `@@`

---

title: Variable Encapsulation

Ruby variables are **always** private. You can only access them through the verbose getters and setters defined by the directives shown previously.

However, any variable can be accessed using the following code:

<script src="https://gist.github.com/4652873.js"></script>

---

title: Class Variables

<script src="https://gist.github.com/4652876.js"></script>

---

title: Class Variables

---

title: Inheritance

<script src="https://gist.github.com/4652877.js"></script>

---

title: Mixins And Modules

Object-oriented languages use inheritance to propagate behavior to similar objects

When the behaviors are not similar, you use [**multiple inheritance**](http://en.wikipedia.org/wiki/Multiple_inheritance) (usually complicated and problematic) or you use something else. 

**Java** uses interfaces to solve this problem. **Ruby** uses modules.

A **module** is a collection of functions and constants. When you include a module as part of a class, those behaviors and constants become part of the class.


---

title: Module Example
content_class: small

<aside class="note" markdown="1">
  <section>
  The ability to write to a file has nothing to do with whether a class is actually a `Person`. We add the capability to add the contents to a file by **mixing in** the capability. We can add new mixins and subclasses to `Person`, and each subclass will have the capabilities of all the mixins without having to know about the mixin’s implementation. 

  Single inheritance plus mixins allow for a nice packaging of behavior.
  </section>
</aside>

<script src="https://gist.github.com/4652878.js"></script>

---

title: Module Example Continued

Note that `to_s` is used in the module but implemented in the class. 

With Java, this contract is **explicit**: the class will implement a formal **interface**

With Ruby, this contract is **implicit**, through **duck typing**

---

title: Comparable

A [**comparable**][comp] class must implement **<=>** (spaceship) operator

[comp]: http://www.ruby-doc.org/core-1.9.3/Comparable.html

<script src="https://gist.github.com/4652879.js"></script>

---

title: Sorting Example

<script src="https://gist.github.com/4652883.js"></script>

---

title: Enumerable

[**enumerable**][enum] include the following methods: `sort`, `any?`, `all?`, `collect` (map), `map`, `flat_map`, `select` (filter), `find`, `max`, `min`, `member?`, `inject` (reduce), `reduce`

<script src="https://gist.github.com/4652885.js"></script>

[enum]: http://ruby-doc.org/core-1.9.3/Enumerable.html

---

title: Inject Example

<script src="https://gist.github.com/4652888.js"></script>

---

title: Questions

Any questions about what we talked about thus far?

---

title: Metaprogramming

Writing programs that write programs.

---

title: Active Record

* [ActiveRecord][] is an [Object Relational Mapping (ORM)][ORM] that is commonly used in Ruby/[Rails][RoR] applications for writing a data abstraction layer for applications.

* `has_many` and `has_one` are Ruby methods that add all the instance variables and methods needed to establish a `has_many` relationship.

<script src="https://gist.github.com/4652891.js"></script>

[RoR]: http://rubyonrails.org/
[ActiveRecord]: http://en.wikipedia.org/wiki/Active_record_pattern
[ORM]: http://en.wikipedia.org/wiki/Object-relational_mapping

---

title: Open Classes

* Ruby classes are never closed to modification. You can always add methods to classes at any time; objects that have been instantiated before the modification can use the new methods. This combined with duck typing is very powerful, but also very dangerous.

* The first invocation of class defines a class; once a class is already defined, subsequent invocations modify that class.

<script src="https://gist.github.com/4652895.js"></script>

---

title: Method_missing

`method_missing` is a debugging method that is called whenever a called method is not available. This can be used to develop a rich, reflective API. Be careful, however, because this means you can no longer debug wrong method calls

<script src="https://gist.github.com/4652898.js"></script>

---

title: Modules

**Macros** are used to change the behavior of a class depending on the environment, taking advantage of inheritance. They can be used to define [Domain Specific Languages (DSL)][DSL] with custom syntax

* **Macro**s and `define_method`: In addition we take another look at **module**s and a Ruby idiom commonly used to provide the same functionality via modules.

[DSL]: http://en.wikipedia.org/wiki/Domain-specific_language

---

title: The Inheritance/Macro Approach

<script src="https://gist.github.com/4652951.js"></script>

---

title: The Module Approach

<script src="https://gist.github.com/4652955.js"></script>

---

title: Strengths

* Purely object oriented (no primitives)
* Duck typing for increased polymorphism
* Can be used somewhat functionally (blocks)
* Web development (see [Ruby on Rails][RoR])
* Good for scripting and being productive quickly
* Prototyping
* Lots of libraries and gems available
* Fun?

[RoR]: http://rubyonrails.org/

---

title: Weaknesses

* Slow (new Ruby VMs try to solve this, see [Rubinius][])
* Stateful programming due to objects make concurrency hard to get right
* Duck typing can be dangerous with regards to type safety, and makes it difficult for developer tools (debuggers, IDEs, etc.) to work with Ruby correctly.

[Rubinius]: http://rubini.us/