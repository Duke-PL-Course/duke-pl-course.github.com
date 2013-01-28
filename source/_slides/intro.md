subtitle: Introduction

---

title: Welcome to House Course 59.18!
subtitle: Programming Languages

### Meeting Time: **Tuesdays** from **4:40** to **7:30 PM**

### Location: **Perkins LINK 2-087 classroom 3**

---

title: Instructors

### Yang Su

![Yang Su](https://sphotos-a.xx.fbcdn.net/hphotos-snc7/432248_10151119162660988_1733947672_n.jpg){: style="max-width: 200px; p#adding: 5px; border: 1px solid #F0F0F0;"}

### Kevin Gao

![Kevin Gao](http://i.imgur.com/epik0.png){: style="max-width: 200px; p#adding: 5px; border: 1px solid #F0F0F0;"}

---

title: Faculty Sponsor

### Robert Duvall
![Robert Duvall](http://www.cs.duke.edu/rcd/images/rcd.jpg)

Lecturer, CS 308

[rcd@cs.duke.edu]('mailto:rcd@cs.duke.edu')

---

title: Questions for You

Mac vs Windows vs Linux?

What other languages have you used?

Experience with Git and Github?

---

title: Website

[http://duke-pl-course.github.com](http://duke-pl-course.github.com)

* Course Information
* Discussion
* Announcements
* Assignments
* Other Resources

---

title: Motivation

Each language has its own set of idioms, its strengths, and its weaknesses.

By learning several different programming languages, you will be able to see which language is best suited to the kinds of problems that interest you most. 

---

title: Prior Knowledge

This is **not** an introductory course to programming.

We assume that everyone is familiar with concepts such as objects, classes, inheritance, polymorphism, functions, and typing. You should be at least comfortable coding in a language like C, C++, Java, or Python.

---

title: Textbook

![Seven Languages in Seven Weeks: A Pragmatic Guide to Learning Programming Languages - Bruce Tate](http://imagery.pragprog.com/products/195/btlang_xlargecover.jpg?1298589937)

[Seven Languages in Seven Weeks - Bruce Tate](http://pragprog.com/book/btlang/seven-languages-in-seven-weeks)

The weekly reading assignments are straight out of the chapters of this book. Some of the assignments will come from the book as well. We will also publish our solutions to all the self study problems after we finish each language. 

---

title: Overview

Languages:

* Ruby
* Io
* Prolog
* Scala
* Erlang
* Clojure
* Haskell

---

title: Why These Languages?
build_lists: true

* Typing Model
* Programming Model
* Implementation
* Core Control and Data Structure
* Unique Features

<aside class="note" markdown="1">
  <section>
    **strong:** types can't be mixed
    **weak:** types can be mixed
    **static:** types checked at compile time
    **dynamic:** types checked during run time
    **duck:** properties and methods determine valid semantics rather than classes and inheritance
    **functional:** functions as basic units of computation and avoids mutable state
    **procedural:** imperative style, list of commands
    **compiled:** generate machine code from source code, and then the machine code gets interpreted
    **interpreted:** source code is interpreted and executed directly by the language interpreter
    **vm:** have a single format for machine code that can run on different machines
  </section>
</aside>

---

title: Language Comparisons
content_class: smaller

Language | Typing Model          | Programming Model | Implementation | Core Control and Data Structure | Unique Features 
-------- | --------------------- | ----------------- | -------------- | ------------------------------- | ---------------
Ruby     | strong, dynamic, duck | OO                | interpreted    | classes, modules                | purely OO, rails, open classes, macros
Io       | weak, dynamic, duck   | prototype         | interpreted    | messages                        | custom syntax, message/object reflection, coroutines, futures
Prolog   | weak, dynamic         | logic based       | compiled       | variables, rules/facts/queries, unification, recursion | solving constraints
Scala    | strong, static        | functional, OO    | compiled, VM   | tuples, pattern matching        | actors, futures, JVM
Erlang   | strong, dynamic       | functional        | compiled, VM   | pattern matching                | "Let it crash", BEAM VM, hotswapping
Clojure  | strong, dynamic       | functional        | compiled, VM   | lazy evaluation, data as code   | macros, versioning, JVM
Haskell  | strong, static        | functional        | compiled       | user-defined types              | purely functional

*[OO]: Object Oriented
*[VM]: Virtual Machine

---

title: Git

![Git](http://git-scm.com/images/logo@2x.png){: style="float: right; margin-left: 10px;"}

We will use Git as the version control system for all the assignments and materials for this course.

Basic usage:

* `git clone`
* `git add`
* `git commit`
* `git push`
* `git pull`
* `git fetch`
* `git rebase`

You can find more information and resources on git under the [resources page](http://duke-pl-course.github.com/resources/#git) on the course website

---

title: Github

![Github Octocat](images/github-logo.png){: style="max-height: 350px; float: left; margin-right: 10px;"}

We will used [github](http://github.com) extensively. 

We have a github organization [Duke-PL-Course](https://github.com/organizations/Duke-PL-Course), which everyone in the class should be a part of.

The source code for [the class website](https://github.com/Duke-PL-Course/duke-pl-course.github.com) and the [class notes](https://github.com/Duke-PL-Course/course-materials) are both open sourced.

Assignments will also be released and tracked through github. More on that later

If you have not used github before, see [help.github.com](https://help.github.com/) for more information.

---

title: Other Tools

Installing all the packages for all 7 languages. Follow the guide [here](http://duke-pl-course.github.com/resources/)

We also recommend Sublime Text 2 for the editor. You can use [this post](http://duke-pl-course.github.com/blog/2013/01/15/setting-up-sublime-text-2/) to set it up.

---

title: Discussion JavaScript vs Io

Language | Advantages | Disadvantages
---------|------------|--------------
JavaScript | Widely Used<br>Large and rapidly growing community<br>Variety of applications and uses (node) | Is not covered in the textbook<br>Is not as flexible as Io
Io | Extremely flexible, light weight syntax<br>Elegant implementations of coroutines, futures, and actors<br>Powerful reflection features | Small community<br>Little syntactical sugar<br>More of a niche language