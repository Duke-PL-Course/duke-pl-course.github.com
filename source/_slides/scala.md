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

title: Functions
class: segue dark

---

title: Declaring a Function

<script src="https://gist.github.com/4974165.js"></script>

A function declaration consists of 4 parts

* The `def` keyword, which defines both a **function** and a **method**
* The **parameters** and their **types**
* An **\*optional\*** return type. Scala can often infer the return type.
* An **expression** or a **block** on the right side of the `=` as the body

To invoke the function, just use the name and the argument list. Unlike Ruby, the parentheses are **not** optional.

---

Functions
You can create functions with def.

scala> def addOne(m: Int): Int = m + 1
addOne: (m: Int)Int
In Scala, you need to specify the type signature for function parameters. The interpreter happily repeats the type signature back to you.

scala> val three = addOne(2)
three: Int = 3
You can leave off parens on functions with no arguments

scala> def three() = 1 + 2
three: ()Int

scala> three()
res2: Int = 3

scala> three
res3: Int = 3

---

title: Function vs Method

A **function** is an **object** with an `apply` method

A **method** generally has less overhead

var + val only gets evaluated once, where as def gets evaluated every time

val o1 = f(List(1, 2, 3))
val o2 = m(List(1, 2, 3))

val o1 = f.apply(List(1, 2, 3))

Functions:
 function literals (two of them, actually) and (T1, T2) => R type signatures

val f = (l: List[Int]) => l mkString ""
val g: (AnyVal) => String = {
  case i: Int => "Int"
  case d: Double => "Double"
  case o => "Other"
}

To convert m to f

val f = m _

Scala will expand that to
val f = new AnyRef with Function1[List[Int], AnyRef] {
  def apply(x$1: List[Int]) = this.m(x$1)
}

Methods have one big advantage (well, two -- they can be slightly faster): they can receive type parameters.

http://stackoverflow.com/questions/2529184/difference-between-method-and-function-in-scala


Aside: Functions vs Methods
Functions and methods are largely interchangeable. Because functions and methods are so similar, you might not remember whether that thing you call is a function or a method. When you bump into a difference between methods and functions, it might confuse you.

scala> class C {
     |   var acc = 0
     |   def minc = { acc += 1 }
     |   val finc = { () => acc += 1 }
     | }
defined class C

scala> val c = new C
c: C = C@1af1bd6

scala> c.minc // calls c.minc()

scala> c.finc // returns the function as a value:
res2: () => Unit = <function0>
When you can call one “function” without parentheses but not another, you might think Whoops, I thought I knew how Scala functions worked, but I guess not. Maybe they sometimes need parentheses? You might understand functions, but be using a method.

In practice, you can do great things in Scala while remaining hazy on the difference between methods and functions. If you’re new to Scala and read explanations of the differences, you might have trouble following them. That doesn’t mean you’re going to have trouble using Scala. It just means that the difference between functions and methods is subtle enough such that explanations tend to dig into deep parts of the language.


---

title: Anonymous Functions

You can create anonymous functions.

scala> (x: Int) => x + 1
res2: (Int) => Int = <function1>
This function adds 1 to an Int named x.

scala> res2(1)
res3: Int = 2
You can pass anonymous functions around or save them into vals.

scala> val addOne = (x: Int) => x + 1
addOne: (Int) => Int = <function1>

scala> addOne(1)
res4: Int = 2
If your function is made up of many expressions, you can use {} to give yourself some breathing room.

def timesTwo(i: Int): Int = {
  println("hello world")
  i * 2
}
This is also true of an anonymous function

scala> { i: Int =>
  println("hello world")
  i * 2
}
res0: (Int) => Int = <function1>
You will see this syntax often used when passing an anonymous function as an argument.

---

title: var vs val

When you declare variables, you should make them immutable whenever you can to avoid conflicting state. In Java, that means using the final keyword. In Scala, immutable means using val instead of var

<script src="https://gist.github.com/4974235.js"></script>

This basic design philosophy is the key element that differentiates functional programming from object-oriented programming: *mutable state limits concurrency*.

---

title: Collections: Lists, Sets, and Maps
class: segue dark

---

title: Lists

A **List** is *an ordered collection of like things with random access*

<script src="https://gist.github.com/4974295.js"></script>

<article markdown="1" class="smaller">
  Operators:

  * `(n)` to access `n`th element
  * `:+` to append an element
  * `++` or `++:` to append a list
  * `::` to prepend an element
  * `:::` to prepend a list
  * `:\` to foldRight. `xs :\ z` is the same as `xs foldRight z`
  * `/:` to foldLeft. `z /: xs` is the same as `xs foldLeft z`

</article>

---

title: Lists Operations

<script src="https://gist.github.com/4974467.js"></script>

---

title: Sets

A **Set** is *an unordered collection of **unique** like things with no explicit order*

<script src="https://gist.github.com/4974423.js"></script>

<article markdown="1" class="smaller">
  Operators:

  * `+` to add an element
  * `-` to remove an element
  * `++` or `|` to compute set union
  * `--` or `&~` to compute set difference
  * `**` or `&` to compute set intersection
  * `:\` to foldRight. `xs :\ z` is the same as `xs foldRight z`
  * `/:` to foldLeft. `z /: xs` is the same as `xs foldLeft z`

</article>

Set operations are **not destructive**. Each set operation *builds a new set* rather than *modifying the old ones*. By default, sets are *immutable*

---

title: Sets Example

<script src="https://gist.github.com/4974341.js"></script>

---

title: Map

A **Map** is *a collection of key-value pairs*, like a Ruby `Hash`

<script src="https://gist.github.com/4974563.js"></script>

<article markdown="1" class="smaller">
  Operators:

  * `(key)` to access the value corresponding to `key`
  * `+` to add 1 or more pairs
  * `++` or `++:` to compute map union
  * `-` to remove 1 or more pairs
  * `--` to compute map difference
  * `:\` to foldRight. `xs :\ z` is the same as `xs foldRight z`
  * `/:` to foldLeft. `z /: xs` is the same as `xs foldLeft z`

</article>

---

title: Map Operations

<script src="https://gist.github.com/4974632.js"></script>

---

title: Mutable Map - HashMap

<script src="https://gist.github.com/4974639.js"></script>

---

title: Any or Nothing

<div style="float: left; margin-right: 10px;" markdown="1">
  ![Type Hiearchy](images/type-hiearchy.png)
</div>

*Everything* inherits from `Any`, and `Nothing` inherits from *everything*.

So a function can return `Nothing` to conform any return type it requires.

`Null` is a `Trait`, and `null` is an instance of it that works like Java’s `null`, meaning an empty value.

By contrast, `Nothing` is a trait that is a subtype of everything.

`Nothing` has no instance, so you can’t dereference it like `Null`. 

For example, a method that throws an Exception has the return type `Nothing`, meaning no value at all.

---

title: Higher-Order Functions
class: segue dark

---

title: Higher-Order Functions

A **higher-order function** is one that takes other *functions as input parameters* or *returns functions as output*

---

title: foreach

The `foreach` method on a collection takes a code block as a parameter in the form of `argument => expression`, which is an *anonymous function*

<script src="https://gist.github.com/4975056.js"></script>

---

title: foreach in Ruby

<script src="https://gist.github.com/4975069.js"></script>

---

title: foreach in JavaScript

<script src="https://gist.github.com/4975165.js"></script>

---

title: More List Methods

<script src="https://gist.github.com/4975177.js"></script>

---

title: Other Higher-Order Functions

<script src="https://gist.github.com/4975192.js"></script>

---

title: The same Example in Ruby

<script src="https://gist.github.com/4975210.js"></script>

---

title: foldLeft

`initialValue /: codeBlock`

val list = List(1, 2, 3)
val sum = (0 /: list) { (sum, i) => sum + i }

 We invoke the operator with a value and a code block. The code block takes two arguments, sum and i.
• Initially, /: takes the initial value, 0, and the first element of list, 1, and passes them into the code block. sum is 0, i is 1, and the result of 0 + 1 is 1.
• Next, /: takes 1, the result returned from the code block, and folds it back into the calculation as sum. So, sum is 1; i is the next element of list, or 2; and the result of the code block is 3.
• Finally, /: takes 3, the result returned from the code block, and folds it back into the calculation as sum. So, sum is 3; i is the next element of list, or 3; and sum+i is 6.

Functional languages use currying to transform a function with multiple parameters to several functions with their own parameter lists. 

list.foldLeft(0)((sum, value) => sum + value)

---

title: fold Practice Problem

Use `foldLeft` or `foldRight` to compute the total size of a list of strings.

---

title: Partially Applied Functions

Partial application
You can partially apply a function with an underscore, which gives you another function. Scala uses the underscore to mean different things in different contexts, but you can usually think of it as an unnamed magical wildcard. In the context of `{ _ + 2 }` it means an unnamed parameter. You can use it like so:

scala> def adder(m: Int, n: Int) = m + n
adder: (m: Int,n: Int)Int
scala> val add2 = adder(2, _:Int)
add2: (Int) => Int = <function1>

scala> add2(3)
res50: Int = 5
You can partially apply any argument in the argument list, not just the last one.

---

title: Curried Functions

Sometimes it makes sense to let people apply some arguments to your function now and others later.

Here’s an example of a function that lets you build multipliers of two numbers together. At one call site, you’ll decide which is the multiplier and at a later call site, you’ll choose a multipicand.

scala> def multiply(m: Int)(n: Int): Int = m * n
multiply: (m: Int)(n: Int)Int
You can call it directly with both arguments.

scala> multiply(2)(3)
res0: Int = 6
You can fill in the first parameter and partially apply the second.

scala> val timesTwo = multiply(2) _
timesTwo: (Int) => Int = <function1>

scala> timesTwo(3)
res1: Int = 6
You can take any function of multiple arguments and curry it. Let’s try with our earlier adder

scala> (adder _).curried
res1: (Int) => (Int) => Int = <function1>

---

title: Variable Length Arguments

There is a special syntax for methods that can take parameters of a repeated type. To apply String’s `capitalize` function to several strings, you might write:

def capitalizeAll(args: String*) = {
  args.map { arg =>
    arg.capitalize
  }
}

scala> capitalizeAll("rarity", "applejack")
res2: Seq[String] = ArrayBuffer(Rarity, Applejack)


---

title: XML
class: segue dark

---


title: Pattern Matching
class: segue dark

---

first class functions
classes and objects
apply method
case classes
generic types and methods
for comprehensions
lazy evaluation
integers, strings are first class objects
