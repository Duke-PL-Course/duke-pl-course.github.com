subtitle: JavaScript

---

title: JavaScript Overview
build_lists: true

JavaScript is ...

* Created by [Brendan Eich][] in 1995 while working for Netscape
* A cross-platform, object-oriented, loosely typed scripting language, designed to run in a host environment (ex: browsers, Node, or other applications)
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

title: Syntax
class: segue dark

---

title: Three Primitive Types

boolean
: `true` or `false`

number
: 64 bit floating number. No integers. Many constants are defined in the Number and Math classes, including `NaN`, `Infinity`, `E`, `PI`, etc.

string
: sequence of zero or more Unicode characters enclosed by `'` or `"`. Characters can be escaped with `\`

---

title: Boolean Values

### Logic Operators

* and: `&&`
* or `||`
* not `!`
* comparisons `>`, `<`, `>=`, `<=` 
* equals `==`, `===`
* not equals `!=`, `!==` 

```javascript
true && true   # > true
true && false  # > false
true || false   # > true
false || false  # > false


```

---

---

title: Falsy Values



---

title: Special Values

Two special values
1. `null`
2. `undefined`

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

var obj = {};
obj['delet']
myHashtable["name"] = "Carl Hollywood";
There is also a dot notation which is a little more convenient.

myHashtable.city = "Anytown";

---

title: Arrays

