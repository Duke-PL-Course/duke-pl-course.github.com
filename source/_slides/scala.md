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
* Interoperable with Java

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
    * VMWare
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

---

title: Expressions and Simple Functions
class: segue dark

---

title: Types

Scala really is **object-oriented**; every value is an object, even what we would call primitives in Java. This includes integers, strings, etc.

Scala [autoboxes and unboxes](autobox) values as necessary.

Scala uses a lot of syntactic sugar to make your life easier, despite everything being an object.

**Infix operators** are just methods in a class that take a single parameter.

[autobox]: http://en.wikipedia.org/wiki/Object_type_(object-oriented_programming)#Autoboxing

---

title: Types (examples)

<script src="https://gist.github.com/sudowork/4760682.js"></script>

---

title: Type Coercion

Like in Ruby, Scala is **strongly** typed, but does a good job of type inference and conversion.

<script src="https://gist.github.com/sudowork/4760760.js"></script>

---

title: Expressions and Conditions

Scala's strong type system means that only `Boolean` values can be evaluated in an `if/else` statement. This is much stricter than Ruby, where everything evaluates to `true` except for `false` and `nil`.


---

expressions and simple functions
first class functions
classes and objects
case classes
pattern matching
generic types and methods
list
for comprehensions
lazy evaluation
