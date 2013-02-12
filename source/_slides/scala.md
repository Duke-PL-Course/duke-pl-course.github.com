subtitle: Scala

---

title: Scala Overview
build_lists: true

Scala is ...

* Created by [Martin Odersky][]
* A [multi-paradigm programming language][multi-paradigm]
    * Object-oriented
    * Funtional
* Its type system is:
    * [Statically][static-typing] typed
    * [Strongly][strong-typing] typed
    * [Structurally][structural-typing] typed
    * Uses [type inference][]
* Built on top of the [Java Virtual Machine][jvm] (JVM)

[Martin Odersky]: http://en.wikipedia.org/wiki/Martin_Odersky
[multi-paradigm]: http://en.wikipedia.org/wiki/Multi-paradigm_programming_language
[static-typing]: http://en.wikipedia.org/wiki/Static_typing#Static_typing
[strong-typing]: http://en.wikipedia.org/wiki/Strong_typing
[structural-typing]: http://en.wikipedia.org/wiki/Structural_type_system
[jvm]: http://en.wikipedia.org/wiki/Jvm
[type inference]: http://en.wikipedia.org/wiki/Type_inference

---

title: Why Learn Scala?

* "General purpose" programming language
* Interoperates with Java
* Many companies are starting to switch to Scala:
    * [Twitter][twitter]'s main message queue
    * [LinkedIn][linkedin]' Social Graph
    * AOL
    * Box
    * eHarmony
    * Foursquare
    * Klout
    * Quora
    * Tumblr
    * [more](http://www.quora.com/Startups/What-startups-or-tech-companies-are-using-Scala)

[twitter]: http://www.scala-lang.org/node/1658#Twitter
[linkedin]: http://www.scala-lang.org/node/7806

---

title: Functional Programming and Concurrency

A major reason why companies are switching to Scala is because it is familiar (Java similarities) and easy to deploy (JVM), but more importantly, it is scalable due to its functional nature.

A **purely functional language** asserts that:
* A function always returns a value
* Given the same inputs, a function will always return the same values
* _Functions will avoid mutating data_

Because data is **immutable**, it is easy to make programs concurrent. A program simply needs to compute a value from some inputs.

Scala is not a purely functional language because it does not guarantee immutability; IO, for example, invalidates the immutability.

---

title: Code Example

<script src="https://gist.github.com/yangsu/4772430.js"></script>

---

title: Expressions and Simple Functions
class: segue dark

---

title: Types

Scala really is **object-oriented**; every value is an object, even what we would call primitives in Java. This includes integers, strings, etc.

Scala [autoboxes and unboxes](autobox) values as necessary.

Scala uses a lot of syntactic sugar to make your life easier, despite everything being an object.

**Infix operators** are just methods in a class that take a single parameter.

Common Scala types include: `Byte`, `Char`, `Short`, `Int`, `Long`, `Float`, `Double`, `Boolean`, and `String`.

There are several classes that augment already existing classes. Ones such as [`StringOps`][stringops], `RichInt`, `RichChar`, etc. that add many more methods to an object. This is usually transparent thanks to **implicit type conversion**.

[autobox]: http://en.wikipedia.org/wiki/Object_type_(object-oriented_programming)#Autoboxing
[stringops]: http://www.scala-lang.org/archives/downloads/distrib/files/nightly/docs/library/index.html#scala.collection.immutable.StringOps

---

title: Numbers and Strings

<script src="https://gist.github.com/sudowork/4760682.js"></script>

---

title: Type Coercion

Like in Ruby, Scala is **strongly** typed, but Scala can also do that type checking at compile time. 

Unlike Java, Scala will use [type inference][] to understand the types of variables through syntactical clues, so you don’t have to type `val a : Int = 1`, though you can if you want.

[type inference]: http://en.wikipedia.org/wiki/Type_inference

---

title: Type Coercion Example

<script src="https://gist.github.com/sudowork/4760760.js"></script>

---

title: Expressions

Expressions can be stored as **values** or **variables**, using the `val` or `var` keywords respectively. In Scala, it is idiomatic to avoid variables; remember, mutable state is bad.

In the REPL, Scala will store unnamed expressions in a value called `res_` where `_` indicates a number.

<script src="https://gist.github.com/4773001.js"></script>

---

title: Boolean Values

Scala's strong type system means that only `Boolean` values can be evaluated in an `if/else` statement. This is much stricter than Ruby, where everything evaluates to `true` except for `false` and `nil`.

<script src="https://gist.github.com/4772536.js"></script>

---

title: Control Structures
class: segue dark

---

title: While Loop

<script src="https://gist.github.com/4772642.js"></script>

We have here defined a function that executes a while loop

Note: unlike in Java, you don’t have to specify `public`. In Scala, `public` is the default visibility, meaning this function will be visible to all.

---

title: For Loop

<script src="https://gist.github.com/4772685.js"></script>

The argument is a variable, followed by the `<-` operator, followed by a range for the loop in the form of `initialValue` until `endingValue`.

---

title: For Each

<script src="https://gist.github.com/yangsu/4772707.js"></script>

`args` is a list with the inbound command-line arguments. Scala passes each element into this block, one by one. In our case, `arg` is one argument from the inbound `args` list. In Ruby, the same code would be `args.each {|arg| println(arg) }.`

---

title: Ranges

* `1 to 10` => `1..10`
* `1 until 10` => `1...10`

<script src="https://gist.github.com/4772723.js"></script>

---

title: Tuples

A **tuple** is a **fixed-length** set of objects of **mixed type**. You’ll find this pattern in many other functional languages as well.

<script src="https://gist.github.com/4772746.js"></script>

---

title: Classes, Inheritance, Traits
class: segue dark

---

title: Classes

Simple Class Definition

<script src="https://gist.github.com/4772791.js"></script>

The same class in Java

<script src="https://gist.github.com/4772823.js"></script>

---

title: Constructor

The whole block of code following the class definition is actually the constructor.

<script src="https://gist.github.com/4772854.js"></script>

---

title: Auxiliary Constructors

Also known as [Constructor Overloading][co] in Java

<script src="https://gist.github.com/4772835.js"></script>

**Note**: the auxiliary constructor calls the primary constructor first with `this(firstName)`

[co]: http://en.wikipedia.org/wiki/Function_overloading#Constructor_overloading

---

title: Companion Objects and Class Methods

In Java and Ruby, you create both **class methods** and **instance methods** within the same body. In Java, class methods have the `static` keyword. Ruby uses `def self.class_method`.

When there’s something that can have only one instance, you’ll define it with the `object` keyword instead of the `class` keyword, which creates a [singleton][] object.

<script src="https://gist.github.com/4772904.js"></script>

In Scala, you can define **class methods** within the **singleton object declaration** and **instance methods** within the **class declaration** of the same name.

[singleton]: http://en.wikipedia.org/wiki/Singleton_pattern

---

title: Inheritance

<script src="https://gist.github.com/4772936.js"></script>

You **must** specify the complete parameter list for Person, though you can omit the types.

The `override` keyword, both in the constructor and for any methods you want to extend from the base class, is **mandatory**. This keyword will keep you from inadvertently introducing new methods with misspellings.

---

title: Traits

Every object-oriented language must solve the problem that one object can have several different roles. C++ uses multiple inheritance, Java uses interfaces, Ruby uses mixins, and Scala uses traits.

A Scala trait is a partial-class implementation that deals with a particular concern, like a Ruby mixin implemented with modules or a Java interface plus an implementation.

<script src="https://gist.github.com/4772960.js"></script>

---


expressions and simple functions
first class functions
classes and objects
apply method
case classes
pattern matching
generic types and methods
list
for comprehensions
lazy evaluation
val vs var
integers, strings are first class objects
