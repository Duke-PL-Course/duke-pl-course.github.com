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

title: Loading Files

Prolog files have the extensions `.pro` or `.pl`. We prefer `.pro` to avoid confusion with Perl files which end in `.pl`.

<script src="https://gist.github.com/4717789.js"></script>

Save a prolog file such as the one above in a directory. Then fire up the Prolog shell with `gprolog` in the same directory.

You should see:

    GNU Prolog 1.4.2
    By Daniel Diaz
    Copyright (C) 1999-2012 Daniel Diaz
    | ?- 

<br>
use `['friends'].` to load the file and you are ready to make queries!

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

title: Queries - Basic Inferences
build_lists: true
fade: true

What if I want to know who's `friends` with Bob?

<script src="https://gist.github.com/4713012.js"></script>

Why did we have to do that?

* Prolog tries to fulfill subgoals in **left-to-right** order.
* The first subgoal: `\+(X = Y)` **always** fails to pass because the expression `<variable> = <atom>` or vice-versa evaluates to `yes`; therefore, the negation of that evaluates to `no`. 
* We need Prolog to first identify possible values for the variable, which is why that subgoal has to be last.

---

title: Example Problem - Map Coloring
class: segue dark

---

title: Map Coloring - Colors

We want to color the Southeastern states, but each bordering state must be a different color.

First, let's declare our colors and state which ones are different:

<script src="https://gist.github.com/4715453.js"></script>

---

title: Map Coloring - States

Next, let's create a rule that enforces each bordering state is different.

<script src="https://gist.github.com/4715462.js"></script>

---

title: Map Coloring - Queries

Let's run a query to get all possible color combinations:

<script src="https://gist.github.com/4715482.js"></script>

---

title: Map Coloring - Queries With Additional Conditions

What if we want to enforce that Alabama must be **red**?

<script src="https://gist.github.com/4715488.js"></script>

---

title: When To Use Prolog?
build_lists: true

* When you have **many possible choices**, but only need to pick **one or more combinations of values** that satisfy a particular problem or constraint.

* Prolog lets you express the **logic** in **facts** and **inferences** and then lets you ask **questions**. You’re not responsible for building any step-by-step imprementation.

* Prolog is not about writing algorithms to solve logical problems. Prolog is about describing your world as it is and presenting logical problems that your computer can try to solve.

---

title: Unification
class: segue dark

---

title: Unification

Unification is performed through the `=` operator. And it can be thought of as two-sided assignment. It is enforcing that the **left** and **right** side of the `=` operator are **equivalent** in the solution.

---

title: Unification Example
build_lists: true

<script src="https://gist.github.com/4716675.js"></script>

* 2 **facts**: `lions` and `tigers` are `cats`
* 2 **rules**:
    * `dorothy/3`, `X`, `Y`, and `Z` are `lion`, `tiger`, and `bear`, respectively.
    * `twin_cats/2`, `X` is a `cat`, and `Y` is a `cat`.

---

title: Unification Example - Queries

<script src="https://gist.github.com/yangsu/4716926.js"></script>

<aside class="note" markdown="1">
  <section>

* We issued the query `twin_cats(One, Two)`. Prolog binds `One` to `X` and `Two` to `Y`. To solve these, Prolog must start working through the goals
* The first goal is `cat(X)`
* We have two facts that match, `cat(lion)` and `cat(tiger)`. Prolog tries the first fact, binding `X` to `lion`, and moves on to the next goal.
* Prolog now binds `Y` to `cat(Y)`. Prolog can solve this goal in exactly the same way as the first, choosing `lion`.
* We’ve satisfied both goals, so the rule is successful. Prolog reports the
values of `One` and `Two` that made it successful and reports `yes`.

  </section>
</aside>

---

title: Practice Problem

[Day 1 Practice Problem](https://github.com/Duke-PL-Course/Prolog/blob/master/2013-02-05-book-problems.md#day-1)

---

title: Recursion
class: segue dark

---

title: Recursion In Prolog

Recursion is essential in Prolog because it's declarative, and therefore, we don't have control structures.

We want to know some things about a family tree. First, let's define our **knowledge base** with a series of facts.

We define a `father` predicate that takes two atoms, with the first atom being the father of the second.


<script src="https://gist.github.com/sudowork/4714249.js"></script>

---

title: Recursion
build_lists: true

<aside class="note" markdown="1">
  <section>

* First clause says "X is the ancestor of Y if X is the father of Y."
* Second clause says "X is an ancestor of Y if we can prove that X is the father of Z and we can also prove that same Z is an ancestor of Y."

  </section>
</aside>

<script src="https://gist.github.com/sudowork/4714251.js"></script>

* Define a `ancestor/2` rule to determine if any 2 atoms are ancestors.

* This rule has 2 **clauses**: the first is the base case of a direct ancestor. The second clause will perform the recursive call.

* When you have multiple clauses that make up a rule, only **1** must be true for the rule to be true. Think of `,` between subgoals as **and** conditions and the `.` between clauses as **or** conditions

* Notice that we can either define the rule twice to achieve multiple clauses, or we can use the logical **OR** `;` to separate clauses.

* Prolog evaluates **top-down**, **left-right**.

---

title: Recursion - Queries

Alright, let's run some queries against our knowledge base:

<script src="https://gist.github.com/sudowork/4714612.js"></script>

---

title: Tail Recursion

Be careful with recursive subgoals as you may end up with too many recursive calls and overflow the stack space.

Declarative languages often solve this problem with a technique called [tail recursion optimization][tro]. 

If you can position the recursive subgoal at the end of a recursive rule, Prolog can optimize the call to discard the call stack, keeping the memory use constant.

[tro]: http://en.wikipedia.org/wiki/Tail_recursion_optimization

---

title: Tuples and Lists
class: segue dark

---

title: Tuples

**Tuples** are containers with a **fixed length**.

Two tuples can unify if they have the same number of elements and each element unifies.

<script src="https://gist.github.com/4717149.js"></script>

---

title: Unification With Tuples

Variables can be on either side of unification

<script src="https://gist.github.com/4717159.js"></script>

---

title: Lists

**Lists** are containers of **variable length**

<script src="https://gist.github.com/4717225.js"></script>

---

title: Deconstructing A List With Unification

**Lists** have a capability that **tuples** don’t. You can deconstruct lists with `[Head|Tail]`. When you unify a list with this construct, `Head` will bind to the **first element** of the list, and `Tail` will bind to the *rest*

<script src="https://gist.github.com/4717288.js"></script>

Note: `[Head|Tail]` won’t unify with an empty list `[]`, but a one-element list is fine.

---

title: Wildcards

<script src="https://gist.github.com/4717347.js"></script>

`_` is a wildcard and unifies with anything. It basically means "I don’t care what’s in this position." 

---

title: Math With Lists
class: segue dark

---

title: Math With Lists - Count
build_lists: true

The count of an empty list `[]` is `0`. The count of a list is the count of the `tail` plus `1`.

<script src="https://gist.github.com/4717401.js"></script>

* We issue the query `count(What, [1])`, which can’t unify with the first rule, because the list is not empty
* We move on to satisfying the goals for the second rule, `count(Count, [Head|Tail])`. We unify, binding `What` to `Count`, `Head` to `1`, and `Tail` to `[]`.
* After unification, the first goal is `count(TailCount, [])`. We try to prove that subgoal. This time, we unify with the first rule. That binds `TailCount` to `0`. The first rule is now satisfied, so we can move on to the second goal.
* Now, we evaluate `Count` is `TailCount + 1`. We can unify variables. `TailCount` is bound to `0`, so we bind Count to `0+1`, or `1`

---

title: Math With Lists - Sum

The sum of an empty list is `0`; the sum of the rest is the `Head` plus the sum of the `Tail`.

<script src="https://gist.github.com/4717428.js"></script>

We haven’t really told Prolog how to compute sums. We’ve merely described sums as rules and goals.

---

title: Math with Lists - Average

As with logic, these rules can build on each other. For example, you can use sum and count together to compute an average

<script src="https://gist.github.com/4717460.js"></script>

The average of List is `Average` if you can prove that

* the sum of that List is `Sum`
* the count of that List is `Count`
* `Average` is `Sum`/`Count`

---

title: append(L1, L2, L3)
class: segue dark

---

title: Making Rules From Rules With Append

The rule `append(List1, List2, List3)` is `true` if `List3` is `List1 + List2`

You can use it to test, combine, or subtract lists, as well as computing list splits.

<script src="https://gist.github.com/4717513.js"></script>

---

title: Rewriting Append - Step 1

To understand `append/3` better, we will write a rule `concatenate/3` to replicate the functionality.

Our first step is to concatenate an empty list `[]` to `List1`

<script src="https://gist.github.com/4717534.js"></script>

---

title: Rewriting Append - Step 2

Then, let’s add a rule that concatenates the **first** element of `List1` to the front of `List2`

<script src="https://gist.github.com/4717545.js"></script>

---

title: Rewriting Append - Step 3

We can define another couple of rules to concatenate lists of lengths 2 and 3. They work in the same way.

<script src="https://gist.github.com/4717562.js"></script>

---

title: Rewriting Append - Step 4

We now have a base case and a strategy where **each subgoal shrinks the first list and grows the third**. The second stays **constant**

To generalize:

<script src="https://gist.github.com/4717589.js"></script>

The first clause says concatenating an empty list to List gives you that List.

The second clause says concatenating `List1` to `List2` gives you `List3` if the heads of `List1` and `List3` are the same, and you can prove that concatenating the tail of `List1` with `List2` gives you the tail of `List3`. 

---

title: Concatenate
build_lists: true

Let's walk through what happens when you execute `concat([1, 2], [3], What)`

* The first rule doesn’t apply, because `[1, 2]` is not `[]`. We unify
to this:  
`concat([1|[2]],[3],[1|Tail2-A]) :- concat([2],[3],[Tail2-A])`  
Everything unifies but `Tail2`. We now move on to the goals
* We try to apply the rule `concat([2], [3], [Tail2-A])`, which results in:  
`concat([2|[]], [3], [2|Tail2-B]) :- concat([], [3], Tail2-B)`  
Notice that `Tail2-B` is the tail of `Tail2-A`. It’s not the same as the original `Tail2`. But now, we have to unify the right side again.
* `concat([], [3], Tail2-C) :- concat([], [3], [3])`
* So, we know `Tail2-C` is `[3]`. Now, we can work back up the chain. Let’s look at the third parameter, plugging in `Tail2` at each step. `Tail2-C` is `[3]`, which means `[2|Tail2-2]` is `[2, 3]`, and finally `[1|Tail2]` is `[1, 2, 3]`. `What` is `[1, 2, 3]`.


---

title: More Recursion And Infinite Answers

<script src="https://gist.github.com/sudowork/4715064.js"></script>

---

title: Practical Prolog With Circuits

<script src="https://gist.github.com/sudowork/4715109.js"></script>

