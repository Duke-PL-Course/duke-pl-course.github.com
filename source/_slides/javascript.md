subtitle: JavaScript

---

title: JavaScript Overview
build_lists: true

JavaScript is ...

* Created by [Brendan Eich][] in 1995 while working for Netscape
* A cross-platform, object-oriented, dynamically typed scripting language, designed to run in a host environment (ex: browsers, Node, or other applications)
* The first [Prototype][] and [lambda][] language to go mainstream
* More closely related to [Self][] or [Scheme][] than C or Java, despite its name

[Brendan Eich]: https://brendaneich.com/
[lambda]: http://en.wikipedia.org/wiki/Lambda_(programming)
[Prototype]: http://en.wikipedia.org/wiki/Prototype-based_programming
[Self]: http://research.sun.com/self/language.html
[Scheme]: http://javascript.crockford.com/little.html

---

title: Code Example

---

title: Data Types
class: segue dark

---

title: Three Primitive Types

boolean

number

string


---

title: Boolean

`true` or `false`

<script src="https://gist.github.com/4667142.js"></script>

---

title: Number

All numbers in JavaScript are **64 bit floating point number**. There are **no integers**. Many constants are defined in the Number and Math classes, including `NaN`, `Infinity`, `Math.E`, `Math.PI`, `Number.MAX_VALUE`, etc.

Most of the math operations you'd expect are supported natively. Many of the utility methods are included in the [`Math`][math] global object.

<script src="https://gist.github.com/4666936.js"></script>

[math]: https://developer.mozilla.org/en-US/docs/JavaScript/Reference/Global_Objects/Math

---

title: String

A string is **a sequence of zero or more Unicode characters** enclosed by `'` or `"`. Characters can be escaped with `\`

`"string"` is equivalent to `new String("string")`

A character is simply a string of length 1

There are many utility methods defined on the [`String`][string] global object

<script src="https://gist.github.com/4667033.js"></script>

[string]: https://developer.mozilla.org/en-US/docs/JavaScript/Reference/Global_Objects/String

---

title: Type Conversion

### Implicit

Because JavaScript is a dynamically and loosely typed language. Differently typed values can be combined without error.

<script src="https://gist.github.com/4667108.js"></script>

### Explicit

You can do type conversion explicitly using prefined functions: `Boolean`, `String`, `Number`, etc.

<script src="https://gist.github.com/4667212.js"></script>

---

title: Special Values

`null`: can be used to denote valid value that represents nothing or emptiness

`undefined`: default value for anything not yet defined or assigned a value

---

title: Logic Operators

* and: `&&`
* or `||`
* not `!`
* comparisons `>`, `<`, `>=`, `<=`
* equals `==`, `===`
* not equals `!=`, `!==`

*Note*: Use `!!` to convert any time to its equivalent boolean value

<script src="https://gist.github.com/4667305.js"></script>

---

title: Falsy Values

* 0
* '' or ""
* null
* undefined
* false
* NaN

<script src="https://gist.github.com/4667307.js"></script>

---

title: Objects And Arrays
class: segue dark

---

title: Objects

Any other data type, such as `Function`, `RegExp`, `Date`, etc., are implemented as objects

An **object** is a basically a hashtable, but none of the hash-table nature (such as hash functions or rehashing methods) is visible.

**Keys** are strings, or other elements such as numbers that are converted to strings

**Values** can be any of the data types, including other objects

---

title: Objects Usage

`{}` is equivalent to `new Object()`. Both create a new object

Use subscript notation or dot notation to add, replace, or retrieve elements in the hashtable.

**Note**: dot notation is limited as you can't look up using reserved words or names that contain dashes

<script src="https://gist.github.com/4667388.js"></script>

---

title: Object References

In JavaScript objects are passed by reference, not value.

<script src="https://gist.github.com/4667415.js"></script>

---

title: Arrays

Arrays in JavaScript are also hashtable objects (The values are located by a key, not by an offset). This makes them very well suited to sparse array applications.

`[]` is equivalent to `new Array()`. Both create an empty array.

Arrays are not typed and dynamic

use `[]` to index into the array and `[]=` to assign values

<script src="https://gist.github.com/4667482.js"></script>

---

title: Variables And Functions
class: segue dark

---

title: Variables

You can declare variables in two ways

* With the keyword `var`. For example, `var x = 42`. This syntax can be used to declare **both local and global variables**
* By simply assigning it a value. For example, `x = 42`. This always declares a global variable and generates a strict JavaScript warning. **You shouldn't use this variant.**

<script src="https://gist.github.com/4667566.js"></script>

---

title: Variable Scope

JavaScript does not have block level scope, only function scope.

<script src="https://gist.github.com/4667668.js"></script>

---

title: Hoisting

All variables within a scope are "hoisted" or lifted to the top of the function or statement.

<script src="https://gist.github.com/4667648.js"></script>

---

title: Global Variables

All variables declared outside of any function, as well as variables declared using direct assignment, reside in the global namespace. the keyword `this` outside side outside of any function refers to the global object.

This is how JavaScript link together libraries to make them easy to uses.

However, this also means that you can overwrite anything in the global scope.

Usually, you should keep all your variables enclosed in a namespace that takes up only **one global variable**

---

title: Functions

A function is a set of statements and expressions enclosed within a special block.

Functions **are objects**, having a hidden, native link to `Function.prototype`.

Functions also have two hidden properties (its context and set of statements that it implements).

Functions are **first-class objects**; they can be used like any other value:
* They can be used as arguments
* They can be stored in data structures (arrays, objects)
* They can be returned
* They can have properties and methods

They are unique in the fact that they can be invoked.

---

title: Writing A Function

A function is made up of four parts:

* The keyword `function`
* An **optional** function name
* A set of parameters wrapped in parentheses
* A block of statements wrapped in curly braces

---

title: Writing A Function

<script src="https://gist.github.com/4667863.js"></script>

---

title: Inner Function

You may write a function literal anywhere an expression may appear.

This means they may appear inside another function; these are called **inner functions**.

An inner function has access to the outer functions parameters and variables.

The collective of the outer function and inner function form a very expressive construct called a **closure**. We will cover closures in a bit.

<script src="https://gist.github.com/4667869.js"></script>

---

title: Invoking A Function

When invoking a function, there are two special parameters that are always included: `this` and `arguments`.

`this` gives the context of a functions invocation

`this` is often a common source of error because it changes based on how a function is invoked.

**invocation** as determined by a parser is a pair of parentheses following an expression that produces a function.

There are four ways to invoke a function:

* Method invocation
* Function invocation
* Constructor invocation
* Apply/call invocation

---

title: Using Method Invocation

<script src="https://gist.github.com/4667876.js"></script>

---

title: Function Invocation

<script src="https://gist.github.com/4667889.js"></script>

---

title: Constructor Invocation

<script src="https://gist.github.com/4667892.js"></script>

---

title: Apply/call Invocation

<script src="https://gist.github.com/4667899.js"></script>

---

title: The Arguments Parameter

In addition to `this`, every function has access to a bonus parameter called `arguments`.

`arguments` is a pseudo-array: it is indexed like an array, has a `length` property, but does not inherit from `Array.prototype`, so it has no array methods

Using the `arguments` parameter in combination with `.call()` or `.apply()` can be a powerful way of using reflection in JavaScript.

One trick to convert arguments into an actual array is as follows:

<script src="https://gist.github.com/4667982.js"></script>

---

title: Returning From A Function

Using `return` from a function will result in the function stopping execution at that point and returning a value.

If no `return` statement is used, then the function will return `undefined`.

If using the **constructor invocation** pattern with the `new` keyword and the return value is not an object, then the returned value will be the newly created object.

<script src="https://gist.github.com/4668082.js"></script>

---

title: Exceptions

**Exceptions** also cause early termination of a function. Surround exception-prone statements with a `try...catch` block.

The `catch` block will be invoked with the exception as a parameter:

<script src="https://gist.github.com/4667987.js"></script>

---

title: Augmenting Types

In JavaScript, you can augment types, just as we did in Ruby with open classes.

To do this, simply modify the type's prototype.

Let's reimplement the times method on `Number`, a la Ruby:

<script src="https://gist.github.com/4668007.js"></script>

---

title: Function Scope

Despite the C/Java-like syntax, JavaScript, does not have **block scope**; instead it *does* have **function scope**.

With block scope, one would normally declare variables as late as possible (at their first use).

When dealing with function scope, it's better practice to declare variables as early as possible.

<script src="https://gist.github.com/4667668.js"></script>

---

title: Closures

Like we talked about, inner functions have access to the parameters and variables of the outer function.

This allows us to create using functions as a **closure**.

A **closure** at its very essence is the combined entity of a function and a set of state. In this case, the inner function acts as the function, and the outer function's parameters and variables allow us to retain state.

---

title: Basic Closure Example

<script src="https://gist.github.com/4668027.js"></script>

---

title: Closures

The variables in a closure can live longer than the life of an inner function. This is both powerful and potentially error-prone:

<script src="https://gist.github.com/4668033.js"></script>

---

title: Callbacks

Use of callbacks in JavaScript is very predominant because of the asynchronous nature of a lot of workflows.

Callback chains can get really messy. You can use libraries to provide better asynchronous control flows:

* [async.js](https://github.com/caolan/async) (uses new control flow constructs)
* [do.js](https://github.com/creationix/do) (uses continuations)
* [jquery.deferred.js](http://jquery.com) (uses promises)

---

title: Callbacks Example

<script src="https://gist.github.com/4668039.js"></script>

---

title: Module Pattern

<script src="https://gist.github.com/4668091.js"></script>

---

title: Cascading Function Calls

<script src="https://gist.github.com/4668114.js"></script>

---

title: Inheritance
class: segue dark

---

title: Prototypal Inheritance

JavaScript, being a loosely typed language, never casts. The lineage of an object is irrelevant. What matters about an object is what it can do, not what it is descended from.

JavaScript is a prototypal language, which means that **objects inherit directly from other objects**.

---

title: Pseudoclassical

We can define a constructor and augment its prototype:

<script src="https://gist.github.com/4668774.js"></script>

---

title: Prototypal

<script src="https://gist.github.com/4668822.js"></script>

---

title: Functional

<script src="https://gist.github.com/4668863.js"></script>

---

title: for...in

JavaScript has support for a control structure known as [`for...in`](https://developer.mozilla.org/en-US/docs/JavaScript/Reference/Statements/for...in).

It allows you to iterate through the enumerable properties of an object in *arbitrary order*.

Be careful, though, because it will go all the way up the prototype chain when searching for enumerable properties. You can use the `hasOwnProperty()` function to filter out properties that belong to an object's prototype.

---

title: for...in Example

<script src="https://gist.github.com/sudowork/4717678.js"></script>

