title: Ruby Overview

Ruby is ...

<ul class="build fade">
  <li>Created by Yukihiro (Matz) Matsumoto</li>
  <li>Interpreted: No compilation necessary, code is executed by an interpreter</li>
  <li>Object-oriented: Everything is an object</li>
  <li>Strongly typed: Types must be compatible or <em>coercible</em></li>
  <li>Dynamically typed: Type checking is performed at run-time</li>
  <li>Duck typed: more on this later</li>
  <li>Commonly used for scripting and web development (Rails)</li>
</ul>


---

title: Code Example

<pre class="prettyprint" data-lang="ruby">
>> properties = ['object oriented', 'duck typed', 'productive', 'fun']
=> ["object oriented", "duck typed", "productive", "fun"]
>> properties.each {|property| puts "Ruby is #{property}."}
Ruby is object oriented.
Ruby is duck typed.
Ruby is productive.
Ruby is fun.
=> ["object oriented", "duck typed", "productive", "fun"]

</pre>

---

title: Purely Object Oriented

_Everything_ in Ruby is an object

<pre class="prettyprint" data-lang="ruby">
42.class      # => Fixnum
42.0.class    # => Float
"foo".class   # => String
[1,2,3].class # => Array

42.methods    # shows the methods available on the object
</pre>

---

title: Typing

In addition to being object-oriented, Ruby is **strongly** and **dynamically** typed

<pre class="prettyprint" data-lang="ruby">
4 + 4       # => 8
4 + "foo"   # results in a TypeError, hence strongly typed
4 + 4.0     # => 8.0      this works because of type coercion

# What about this though?
def add_stuff
  4 + 4.0
end # => nil

add_stuff # => TypeError    This proves that Ruby is dynamically typed
</pre>

---

title: Duck Typing

The duck test:

<blockquote>
  "If it looks like a duck, swims like a duck, and quacks like a duck, then it probably is a duck."
</blockquote>

<br>

Ruby is duck-typed, meaning that if two objects of different classes have the same method signature, then they can be used together.

<pre class="prettyprint" data-lang="ruby">
i = 0
a = ['100', 100.0, '50', 50.0]
while i < a.size
  <b>puts a[i].to_i</b>
  i = i + 1
end
</pre>

---

title: Variables

<pre class="prettyprint" data-lang="ruby">
foo = 'hello, plcourse' # here we define a function. Notice there's no type declaration
foo = 'is mutable'      # variables are mutable, i.e. they can vary
CONSTANTS = 'are defined like this' # they are immutable
</pre>

---

title: Ranges

* inclusive `1..3`
* exclusive `1...3`

---

title: Functions

<pre class="prettyprint" data-lang="ruby">
puts(foo)               # this prints "hello, plcourse" and returns nil
puts foo                # this is exactly the same as above, with a bit of syntactic sugar
</pre>

We saw a bit of defining a function earlier in add_stuff

Notice that you didn't need to specify parameter types, return types, or even a return statement

**Every function returns something**. If you do not specify an explicit return, the function will return the value of the last expression that’s processed before exiting.

<pre class="prettyprint" data-lang="ruby">
def be_truthful
  42
  true    # The last expression is always the one that gets returned
end
</pre>

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

title: Tricky precedence nuance

* Don't use `or`, `and`, or `not` when dealing with assignment, and don't mix `&&` and `||` with `and` and `or`.
* Why? `and`, `or`, and `not` are lower precedence than assignment.
* So when is it okay to use them?

Why not use them?

<pre class="prettyprint" data-lang="ruby">
>> foo = false or true    # This expression evaluates to true
=> true
>> foo                    # But it assigned foo to false
=> false
</pre>

---

title: Control Structures

### Expression modifiers
`if`, `unless`, `while`, `until`

### Falsy Values
everything but `nil` and `false` evaluate to true. `0` is true!

---

title: Arrays

Arrays in Ruby can contain mixed types

<pre class="prettyprint" data-lang="ruby">
[1, "two", 3] # is perfectly valid
Array.new     # remember, these are objects, and objects can be instantiated
              #   with .new()

cars = ['ford', 'toyota', 'subaru']
cars[0]     # => "ford"
cars[2]     # => "subaru"
cars[-1]    # => "subaru"
cars[-4]    # => nil
cars[9001]  # => nil
cars[1..2]  # => ["toyota", "subaru"]
cars[1..2]  # => ["toyota", "subaru"]
cars[0...2] # => ["ford", "toyota"]
cars.[](0...2)# => ["ford", "toyota"]
</pre>

---

title: More Arrays

`[]` and `[]=` are just methods of the Array class; their typical usage is just syntactic sugar

Multidimensional arrays are just arrays of arrays

`push`, `pop`, as well as other functions exist natively in the [Array API][Array] that allow arrays to be used as queues, linked lists, stacks, or sets.

---

title: Hashes/Maps

<pre class="prettyprint" data-lang="ruby">

# Literal Form
numbers = { 1 => 'one', 2 => 'two' }
# => {1=>"one", 2=>"two"}

# Accessing element using key
numbers[1] # => "one"

# Can use symbols as keys
stuff = { :array => [1, 2, 3], :string => 'Hello' }
# => {:array=>[1, 2, 3], :string=>"Hello"}

# Accessing element using key
stuff[:string] # => "Hello"
</pre>

**symbol**s are identifying values/objects. Two symbols of the same name always refer to the same object id

---

title: Named Parameters

Hashes can be used to implement Named Parameters

<pre class="prettyprint" data-lang="ruby">
def tell_the_truth(options={})
  if options[:profession] == :lawyer
    'it could be believed that this is almost certainly not false.'
  else
    true
  end
end

tell_the_truth
=> true
tell_the_truth( :profession => :lawyer )
=> "it could be believed that this is almost certainly not false.
</pre>

---

title: Code blocks

`{ ... }` code between braces is a code block; alternavitely, `do ... end` (usually for multi-line blocks) syntax can be used

`Fixnum.times` can be used to loop a certain number of times: `3.times { puts 'Hello, World!' }`

Use `each` on a collection (Array or Hash) to iterate over the elements in the collection: `animals.each { |a| puts a }` and `numbers.each { |k,v| puts "#{k} maps to #{v}" }`

---

title: Yielding

Augmenting a class definition and using **yield** to call a block

<pre class="prettyprint" data-lang="ruby">
class Fixnum
  def my_times
    i = self
    while i > 0
      i -= 1
      yield
    end
  end
end
</pre>

---

title: Call

Alternatively, call a block using `call`. When we do this, the block is actually an instance of `Proc` (short for procedure). The main difference is that a Proc can be stored.

Useful for policy enforcement, conditional execution, transactions, etc.

---

title: Code for Call
content_class: small

<pre class="prettyprint" data-lang="ruby">
def call_block(&block)  # NOTE: block is actually an instance of Proc
  block.call 1, 2
end
call_block { |a,b| puts "Hello #{a} and #{b}" } # "Hello 1 and 2"

def yield_params
  yield 1, 2
end
yield_params { |a,b| puts "#{a} and #{b}" } # "1 and 2"

# Example of instantiating a proc
someProc = Proc.new do
  # do stuff here
end
otherProc = lambda do
  # do other stuff here
end
puts someProc.class   # Proc
puts otherProc.class  # Proc
</pre>

---

title: Classes

* Classes start with capital letters and typically use `CamelCase` to denote capitalization
* You must prepend instance variables (one value per object) with `@` and class variables (one value per class) with `@@`
* Instance variables and method names begin with lowercase letters in the `underscore_style`. Constants are in `ALL_CAPS`
* Functions and methods that test typically use a question mark (`if test?`)
* The `attr` keyword defines an instance variable. Several versions exist. The most common are attr (defining an instance variable and a method of the same name to access it) and `attr_accessor`, defining an instance variable, an accessor, and a setter

---

title: Sample Tree Implementation

[Source](https://github.com/Duke-PL-Course/Ruby/blob/master/examples/2013-01-15-tree.rb)

---

title: Mixins and Modules

Object-oriented languages use inheritance to propagate behavior to similar objects. When the behaviors are not similar, you use multiple inheritance (usually complicated and problematic) or you use something else. Java uses interfaces to solve this problem. Ruby uses modules.

A module is a collection of functions and constants. When you include a module as part of a class, those behaviors and constants become part of the class.

---

title: Module Example
content_class: small

<pre class="prettyprint" data-lang="ruby">
module ToFile
  def filename "object_#{self.object_id}.txt" end
  def to_f File.open(filename, 'w') {|f| f.write(to_s)} end
end
class Person
  include ToFile
  attr_accessor :name
  def initialize(name) @name = name end
  def to_s name end
end
Person.new('Kevin').to_f
</pre>

Note that `to_s` is used in the module but implemented in the class. With Java, this contract is explicit: the class will implement a formal interface. With Ruby, this contract is implicit, through duck typing.

---

title: Modules, Enumerable, and Sets

* **enumerable** and **comparable** are important modules/mixins.
* A **comparable** class must implement **<=>** (spaceship) operator
* [**enumerable**][Enumerable] include the following methods: `sort`, `any?`, `all?`, `collect` (map), `map`, `flat_map`, `select` (filter), `find`, `max`, `min`, `member?`, `inject` (reduce), `reduce`

---

title: Day 3: Serious Change

**Metaprogramming**: writing programs that write programs.

### Active Record
* [_ActiveRecord_][ActiveRecord] is an [Object Relational Mapping (ORM)][ORM] that is commonly used in Ruby/[Rails][RoR] applications for writing a data abstraction layer for applications.

* `has_many` and `has_one` are Ruby methods that add all the instance variables and methods needed to establish a `has_many` relationship.

```ruby
class Department < ActiveRecord::Base
  has_many :employees
  has_one :manager
end
```

### Open classes
* Ruby classes are never closed to modification. You can always add methods to classes at any time; objects that have been instantiated before the modification can use the new methods. This combined with duck typing is very powerful, but also very dangerous.

* The first invocation of class defines a class; once a class is already defined, subsequent invocations modify that class.

```ruby
class NilClass
  def blank?
    true
  end
end

class String
  def blank?
    self.size == 0
  end
end

["", "person", nil].each do |element|
  puts element unless element.blank?
end
```

### Via `method_missing`
* `method_missing` is a debugging method that is called whenever a called method is not available. This can be used to develop a rich, reflective API. Be careful, however, because this means you can no longer debug wrong method calls. An example of such an API is shown below:

    ```ruby
    class Roman
      def self.method_missing name, *args
        roman = name.to_s
        roman.gsub!("IV", "IIII")
        roman.gsub!("IX", "VIIII")
        roman.gsub!("XL", "XXXX")
        roman.gsub!("XC", "LXXXX")
        (roman.count("I") +
         roman.count("V") * 5 +
         roman.count("X") * 10 +
         roman.count("L") * 50 +
         roman.count("C") * 100)
      end
    end
    puts Roman.X    # 10
    puts Roman.XC   # 90
    puts Roman.XII  # 12
    puts Roman.IX   # 9
    ```

### Modules
**Macros** are used to change the behavior of a class depending on the environment, taking advantage of inheritance. They can be used to define [Domain Specific Languages (DSL)][DSL] with custom syntax

* **Macro**s and `define_method`: In addition we take another look at **module**s and a Ruby idiom commonly used to provide the same functionality via modules.

#### The inheritance/macro approach
```ruby
class Person
  attr_accessor :name
  def self.can_speak  # This is a class method! Notice the self.
    define_method 'speak' do  # an instance method
      puts "I can talk, my name is #{@name}!"
    end
  end

  def initialize(name)
    @name = name
  end
end

class Guy < Person
  can_speak
end

class ShyGuy < Person
end

john = Guy.new('John')
bob = ShyGuy.new('Bob')
john.methods.include?(:speak)   # true
bob.methods.include?(:speak)    # false
```

#### The module approach
```ruby
module Person
  attr_accessor :name
  def self.included(base) # included is invoked whenever a module is included; base is implicit
    base.extend ClassMethods  # extend will add the methods defined in ClassMethods as class methods
  end
  module ClassMethods
    def can_speak
      include InstanceMethods # This includes all the instance methods
    end
  end
  module InstanceMethods
    def speak
      puts "I can talk, my name is #{@name}!"
    end
  end
  def initialize(name)
    @name = name
  end
end

class Guy
  include Person
  can_speak
end

class ShyGuy
  include Person
end

john = Guy.new('John')
bob = ShyGuy.new('Bob')
john.methods.include?(:speak)   # true
bob.methods.include?(:speak)    # false
```

## Wrapping Up

### Strengths
* Purely object oriented (no primitives)
* Duck typing for increased polymorphism
* Can be used somewhat functionally (blocks)
* Web development (see [Ruby on Rails][RoR])
* Good for scripting and being productive quickly
* Prototyping
* Lots of libraries and gems available
* Fun?

### Weaknesses
* Slow (new Ruby VMs try to solve this, see [Rubinius][])
* Stateful programming due to objects make concurrency hard to get right
* Duck typing can be dangerous with regards to type safety, and makes it difficult for developer tools (debuggers, IDEs, etc.) to work with Ruby correctly.

<!-- Links -->

[Interpreted]: http://en.wikipedia.org/wiki/Interpreted_language
[Object-oriented]: http://en.wikipedia.org/wiki/Object-oriented_programming
[Strongly typed]: http://en.wikipedia.org/wiki/Strong_typing
[Dynamically typed]: http://en.wikipedia.org/wiki/Type_system#Dynamic_typing
[Duck typed]: http://en.wikipedia.org/wiki/Duck_typing
[Array]: http://www.ruby-doc.org/core-1.9.3/Array.html
[Proc]: http://www.ruby-doc.org/core-1.9.3/Proc.html
[Enumerable]: http://ruby-doc.org/core-1.9.3/Enumerable.html
[RoR]: http://rubyonrails.org/
[Rubinius]: http://rubini.us/
[DSL]: http://en.wikipedia.org/wiki/Domain-specific_language
[ActiveRecord]: http://en.wikipedia.org/wiki/Active_record_pattern
[ORM]: http://en.wikipedia.org/wiki/Object-relational_mapping
