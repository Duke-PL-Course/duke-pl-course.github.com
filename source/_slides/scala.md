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

---

title: Affinity with Java...

Scala is at least a bridge and maybe more. It offers tight integration into Java, offering a chance for people to protect their investment in many ways:

* Scala runs on the Java virtual machine, so Scala can run side-by-side with existing deployments.
* Scala can use Java libraries directly, so developers can leverage existing frameworks and legacy code.
* Like Java, Scala is statically typed, so the languages share a philosoph- ical bond.
* Scala’s syntax is relatively close to Java’s, so developers can learn the basics quickly.
* Scala supports both object-oriented and functional programming paradigms, so programmers can gradually learn to apply functional programming ideas to their code.

---

title: Departures from Java

* **Type inference**. In Java, you must declare the type of every variable, argument, or parameter. Scala infers variable types where possible.
* **Functional concepts**. Scala introduces important functional concepts to Java. Specifically, the new language allows you to use existing functions in many different ways to form new ones. Concepts you’ll see in this chapter are code blocks, higher-order functions, and a sophisticated collection library. Scala goes far beyond some basic syntactical sugar.
* **Immutable variables**. Java does allow immutable variables but with a rarely used modifier. In this chapter, you’ll see that Scala forces you to explicitly make a decision about whether a variable is mutable. These decisions will have a profound effect on how applications behave in a concurrent context.
* **Advanced programming constructs**. Scala uses the foundational language well, layering on useful concepts. In this chapter, we’ll introduce you to actors for concurrency, Ruby-style collections with higher-order func- tions, and first-class XML processing.

---

integers, strings are first class objects

---

Scala is actually strongly typed. Scala will use type inference, so most of the time, it will understand the types of variables through syntactical clues, but unlike Ruby, Scala can do that type checking at compile time. 

But unlike Java, Scala can infer the type, so you don’t have to type val a : Int = 1, though you can if you want.

---

title: Expressions and Conditions

scala> 5 < 6
res27: Boolean = true
scala> 5 <= 6
res28: Boolean = true
scala> 5 <= 2
res29: Boolean = false
scala> 5 >= 2
res30: Boolean = true
scala> 5 != 2
res31: Boolean = true

scala> val a = 1 a: Int = 1
scala> val b = 2 b: Int = 2
scala> if ( b < a) {
| println("true")
| } else {
| println("false") |}
false

---

title: Boolean values

In Ruby, `0` evaluated to `true`. In C, `0` was `false`. In both languages, `nil` evaluated to `false`. Let’s see how Scala handles them:

scala> Nil
res3: Nil.type = List()
scala> if(0) {println("true")} <console>:5: error: type mismatch;
 found   : Int(0)
 required: Boolean
       if(0) {println("true")}
          ^
scala> if(Nil) {println("true")} <console>:5: error: type mismatch;
 found   : Nil.type (with underlying type object Nil)
 required: Boolean
       if(Nil) {println("true")}

So, a Nil is an empty list, and you can’t even test Nil or 0. This behavior is consistent with Scala’s strong, static typing philosophy. Nils and numbers are not booleans, so don’t treat them like booleans.

---

title: Loops

---

title: While Loop

def whileLoop {
    var i = 1
    while(i <= 3) {
        println(i)
        i += 1
    }
}
whileLoop
So, a Nil is an empty list, and you can’t even test Nil or 0. This behavior is consistent with Scala’s strong, static typing philosophy. Nils and numbers are not booleans, so don’t treat them like booleans.

---

title: For Loop

def forLoop {
    println( "for loop using Java-style iteration" )
    for(i <- 0 until args.length) {
        println(args(i))
    }
}
 
forLoop

The argument is a variable, followed by the <- operator, followed by a range for the loop in the form of initialValue until endingValue.

---

title: foreach

def rubyStyleForLoop {
    println( "for loop using Ruby-style iteration" )
    args.foreach { arg => 
        println(arg)
    }
}
 
rubyStyleForLoop

---

title: Ranges

Like Ruby, Scala supports first-class ranges.

1 to 10 => 1..10
1 until 10 => 1...10

scala> val range = 0 until 10
range: Range = Range(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
scala> range.start
res2: Int = 0
scala> range.end
res3: Int = 10
scala> range.step
res4: Int = 1
scala> (0 to 10) by 5
res6: Range = Range(0, 5, 10)
scala> (0 to 10) by 6
res7: Range = Range(0, 6)
scala> (0 until 10 by 5)
res0: Range = Range(0, 5)
scala> val range = (10 until 0) by -1
range: Range = Range(10, 9, 8, 7, 6, 5, 4, 3, 2, 1)
scala> val range = (10 until 0)
range: Range = Range()
scala> val range = (0 to 10)
range: Range.Inclusive = Range(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

---

title: Tuples

A tuple is a fixed-length set of objects. You’ll find this pattern in many other functional languages as well. The objects in a tuple can all have different types.

scala> val person = ("Elvis", "Presley")
person: (java.lang.String, java.lang.String) = (Elvis,Presley)
scala> person._1
res9: java.lang.String = Elvis
scala> person._2
res10: java.lang.String = Presley
scala> person._3
<console>:6: error: value _3 is not a member of (java.lang.String, java.lang.String)
person._3

Scala uses tuples rather than lists to do multivalue assignments:
scala> val (x, y) = (1, 2) x: Int = 1
y: Int = 2
Since tuples have a fixed length, Scala can do static type checking based on each of the tuple values:
scala> val (a, b) = (1, 2, 3)
<console>:9: error: constructor cannot be instantiated to expected type;
 found   : (T1, T2)
 required: (Int, Int, Int)
       val (x, y) = (1, 2, 3)
           ^
<console>:9: error: recursive value x$1 needs type
       val (x, y) = (1, 2, 3)

---

title: Classes

class Person(firstName: String, lastName: String)
val gump = new Person("Forrest", "Gump")

The whole block of code following the class definition is actually the con- structor.

class Person(firstName: String) {
  println("Outer constructor")
  def this(firstName: String, lastName: String) {
    this(firstName)
    println("Inner constructor")
  }
  def talk() = println("Hi")
}
val bob = new Person("Bob")
val bobTate = new Person("Bob", "Tate")

---

title: Extending Classes

Companion Objects and Class Methods

In Java and Ruby, you create both class methods and instance methods within the same body. In Java, class methods have the static keyword. Ruby uses def self.class_method.

When there’s something that can have only one instance, you’ll define it with the object keyword instead of the class keyword.

object TrueRing {
def rule = println("To rule them all")
}
TrueRing.rule

The TrueRing definition works exactly like any class definition, but it creates a singleton object. In Scala, you can have both an object definition and a class definition with the same name. Using this scenario, you can create class methods within the singleton object declaration and instance methods within the class declaration.

---

title: Inheritance

Inheritance in Scala is pretty straightforward, but the syntax must be exact. Here’s an example of extending a Person class with Employee. Notice that the Employee has an additional employee number in the id field.

class Person(val name: String) {
  def talk(message: String) = println(name + " says " + message)
  def id(): String = name
}
 
class Employee(override val name: String, 
                        val number: Int) extends Person(name) {
  override def talk(message: String) {
    println(name + " with number " + number + " says " + message)
  }
  override def id():String = number.toString
} 
 
val employee = new Employee("Yoda", 4)
employee.talk("Extend or extend not. There is no try.")

Notice that you must specify the complete parameter list for Person, though you can omit the types.

The override keyword, both in the constructor and for any methods you want to extend from the base class, is mandatory. This keyword will keep you from inadvertently introducing new methods with misspellings.

---

title: Traits

C++ uses multiple inheritance, Java uses interfaces, Ruby uses mixins, and Scala uses traits. A Scala trait is like a Ruby mixin, implemented with modules. Or, if you prefer, a trait is like a Java interface plus an implementation.
Look at a trait as a partial-class implementation. Ideally, it should implement one critical concern.

---

title: val vs var