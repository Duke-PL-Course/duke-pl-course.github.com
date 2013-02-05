subtitle: Prolog

---

title: Prolog Overview
build_lists: true

Prolog is ...

* developed in 1972 by Alain Colmerauer and Phillipe Roussel
* a general purpose [logic programming][] language associated with [artificial intelligence][] and [computational linguistics][]
* a [declarative language][], meaning you don't specify the control flow and that it bases its computations on programmer-provided facts and inferences and then deduces the result

[logic programming]: http://en.wikipedia.org/wiki/Logic_programming
[artificial intelligence]: http://en.wikipedia.org/wiki/Artificial_intelligence
[computational linguistics]: http://en.wikipedia.org/wiki/Computational_linguistics
[declarative language]: http://en.wikipedia.org/wiki/Declarative_programming

---

title: Code Example

<script src="https://gist.github.com/4712393.js"></script>

---

title: Basics
class: segue dark

---

title: Building Blocks
build_lists: true
fade: true

* Facts
: A basic assertion about some world

* Rules
: An inference about the facts in that world

* Query
: A question about that world

* Atom
: word that begins with a *lowercase* letter

* Variable
: word that begins with a *uppercase* letter or an *underscore*

* **Facts** and **rules** will go into a **knowledge base**. A Prolog compiler compiles the knowledge base into a form that’s efficient for **queries**.

---

title: Facts

A **fact** is a basic assertion about some world. 

Ex. Babe is a pig; pigs like mud.

Format of a fact: `<predicate>(<atom>, ...)`

<script src="https://gist.github.com/4712431.js"></script>

---

title: Rules
build_lists: true
fade: true

A **rule** is an inference about the facts in that world. 

Ex. An animal likes mud if it is a pig.

<script src="https://gist.github.com/4712509.js"></script>

* The above rule is called `friend/2` (name of friend and takes two parameters)
* `X`, `Y`, and `Z` are variables.
* The `:-` is the declaration operator. In this case, we are declaring a rule
* Everything to the right of the `:-` are considered the **subgoal**s. The subgoals are separated by a `,`, this signifies a logical **AND**
* `\+` is the negation operator. We are stating that `X` cannot equal `Y`; you cannot be a friend of yourself
* The two other subgoals are that `X` must like atom `Z`, and in addition, `Y` must also like atom `Z`

---

title: Queries - Simple Boolean Queries
build_lists: true
fade: true

A **query** is a question about that world.

Ex. Does Babe like mud?

<script src="https://gist.github.com/4712513.js"></script>

`friend(alice, alice)` violates the first subgoal, `no` is returned

`friend(bob, charlie)`:

* Try multiple values for `X`, `Y`, and `Z` respectively: `bob, charlie, chocolate` and `bob, charlie, cheese`
* For the first set, we see that `likes(Y, Z)` is `true`, but `likes(X, Z)` is false. So this cannot be a valid solution
* For the next set, all subgoals are satisfied, so `yes` is returned

---

title: Queries - With Variables

What if we don't want a `yes` or `no` answer? We can ask `What` or `Who`

<script src="https://gist.github.com/4712807.js"></script>

The interpreter will show one result, then expect either `;`, `a`, or `RETURN` after executing the query

* `;` for next solution
* `a` for all solutions
* `RETURN` to stop

`What`, `Who`, and `X` mean exactly the same thing. They are variables, signified by the capital letter at the beginning.

---

title: Queries

What if I want to know who's `friends` with Bob?

<script src="https://gist.github.com/4713012.js"></script>

Why did we have to do that?

* Prolog tries to fulfill subgoals in **left-to-right** order.
* The first subgoal: `\+(X = Y)`, 
* It happens that the expression `<variable> = <atom>` or vice-versa evaluates to `yes`; therefore, the negation of that evaluates to `no`. 
* So the first subgoal always fails to pass. 
* We need Prolog to first identify possible values for the variable, which is why that subgoal has to be last.

---



---

### Map Coloring
We want to color the Southeastern states, but each bordering state must be a different color.

First, let's declare our colors and state which ones are different:

```prolog
% Notice that order matters, so we have duplicate combinations
different(red, green). different(red, blue).
different(green, red). different(green, blue).
different(blue, red). different(blue, green).
```

Next, let's create a rule that enforces each bordering state is different.

```prolog
coloring(Alabama, Mississippi, Georgia, Tennessee, Florida) :-
  different(Mississippi, Tennessee),
  different(Mississippi, Alabama),
  different(Alabama, Tennessee),
  different(Alabama, Mississippi),  % This one is unnecessary (redundant information)
  different(Alabama, Georgia),
  different(Alabama, Florida),
  different(Georgia, Florida),
  different(Georgia, Tennessee).
```

---

Let's run a query to get all possible color combinations:

```prolog
| ?- coloring(Alabama, Mississippi, Georgia, Tennesse
e, Florida).

Alabama = blue
Florida = green
Georgia = red
Mississippi = red
Tennessee = green ? a
...
```

What if we want to enforce that Alabama must be red?

```prolog
| ?- coloring(Alabama, Mississippi, Georgia, Tennesse
e, Florida), Alabama = red.

Alabama = red
Florida = blue
Georgia = green
Mississippi = green
Tennessee = blue ? a
...
```

---

So, when should I use Prolog? Have you ever run into a situation where you have a bunch of possible choices, but you need to pick one or more combinations of values that satisfy a particular problem? Prolog takes care of the algorithmic part of it for you, you just have to put in the constraints!
**<a href="#unification">Unification</a>**: Unification is performed through the `=` operator. And it can be thought of as assignment. It is enforcing that the left and right side of the `=` operator are equivalent in the solution.

---

title: Recursion in Prolog

Recursion is essential in Prolog because it's declarative, and therefore, we don't have control structures.

We want to know some things about a family tree. First, let's define our **knowledge base** with a series of facts.

We define a `father` predicate that takes two atoms, with the first atom being the father of the second.

<script src="https://gist.github.com/sudowork/4714249.js"></script>

---

title: Recursion

Now, we want to define our `ancestor/2` rule to determine if any two atoms are ancestors.

This rule will have two **clauses**: the first being the base case of being a direct ancestor. The second clause will perform the recursive call.

<script src="https://gist.github.com/sudowork/4714251.js"></script>

Notice that we can either define the rule twice to achieve multiple clauses, or we can use the logical **OR** `;` to separate clauses.

Note that Prolog evaluates top-down, left-right.

---

title: Recursion - Queries

Alright, let's run some queries against our knowledge base:

<script src="https://gist.github.com/sudowork/4714612.js"></script>

---

title: Tuples

---

title: Unification with tuples

**Unification** is like two-way pattern matching.

...

---

title: Lists

---

title: Deconstructing a list with unification

---

title: Math with lists

---

title: Making rules from rules with append

---

title: Rewriting append

---

title: More recursion and infinite answers

<script src="https://gist.github.com/sudowork/4715064.js"></script>

---

title: Practical Prolog with circuits

<script src="https://gist.github.com/sudowork/4715109.js"></script>

