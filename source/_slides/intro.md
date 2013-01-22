title: Welcome to House Course 59.18!
subtitle: Programming Languages

### Meeting Time: **Tuesdays** from **4:40** to **7:30 PM**

### Location: **Perkins LINK 2-087 classroom 3**

---

title: Instructors

### Yang Su

<img src="https://sphotos-a.xx.fbcdn.net/hphotos-snc7/432248_10151119162660988_1733947672_n.jpg" alt="" style="max-width: 200px; p#adding: 5px; border: 1px solid #F0F0F0;">

### Kevin Gao

<img src="http://i.imgur.com/epik0.png" alt="" style="max-width: 200px; p#adding: 5px; border: 1px solid #F0F0F0;">

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

<aside class="note">
  <section>
    <strong>strong:</strong> types can't be mixed<br>
    <strong>weak:</strong> types can be mixed<br>
    <strong>static:</strong> types checked at compile time<br>
    <strong>dynamic:</strong> types checked during run time<br>
    <strong>duck:</strong> properties and methods determine valid semantics rather than classes and inheritance<br>
    <strong>functional:</strong> functions as basic units of computation and avoids mutable state<br>
    <strong>procedural:</strong> imperative style, list of commands<br>
    <strong>compiled:</strong> generate machine code from source code, and then the machine code gets interpreted<br>
    <strong>interpreted:</strong> source code is interpreted and executed directly by the language interpreter<br>
    <strong>vm:</strong> have a single format for machine code that can run on different machines<br>
  </section>
</aside>

---

title: Language Comparisons
content_class: smaller

<table>
  <tr>
    <th></th>
    <th>Typing Model</th>
    <th>Programming Model</th>
    <th>Implementation</th>
    <th>Core Control and Data Structure</th>
    <th>Unique Features</th>
  </tr>
  <tr>
    <td>Ruby</td>
    <td>strong, dynamic, duck</td>
    <td>object oriented</td>
    <td>interpreted</td>
    <td>classes, modules</td>
    <td>purely object oriented, rails, open classes, macros</td>
  </tr>
  <tr>
    <td>Io</td>
    <td>weak, dynamic, duck</td>
    <td>prototype</td>
    <td>interpreted</td>
    <td>messages</td>
    <td>custom syntax, message/object reflection, coroutines, futures</td>
  </tr>
  <tr>
    <td>Prolog</td>
    <td>weak, dynamic</td>
    <td>logic based</td>
    <td>compiled</td>
    <td>variables, rules/facts/queries, unification, recursion</td>
    <td>solving constraints </td>
  </tr>
  <tr>
    <td>Scala</td>
    <td>strong, static</td>
    <td>functional, object oriented</td>
    <td>compiled, virtual machine</td>
    <td>tuples, pattern matching</td>
    <td>actors, futures, JVM</td>
  </tr>
  <tr>
    <td>Erlang</td>
    <td>strong, dynamic</td>
    <td>functional</td>
    <td>compiled, virtual machine</td>
    <td>pattern matching</td>
    <td>"Let it crash", BEAM VM, hotswapping</td>
  </tr>
  <tr>
    <td>Clojure</td>
    <td>strong, dynamic</td>
    <td>functional</td>
    <td>compiled, virtual machine</td>
    <td>lazy evaluation, data as code</td>
    <td>macros, versioning, JVM</td>
  </tr>
  <tr>
    <td>Haskell</td>
    <td>strong, static</td>
    <td>functional</td>
    <td>compiled</td>
    <td>user-defined types</td>
    <td>purely functional</td>
  </tr>
</table>

---

title: Git

<img src="http://git-scm.com/images/logo@2x.png" alt="Git" style="float: right; margin-left: 10px;">

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

<img src="images/github-logo.png" alt="Github Octocat" style="max-height: 350px; float: left; margin-right: 10px;">

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

<table>
  <tr>
    <th></th>
    <th>Advantages</th>
    <th>Disadvantages</th>
  </tr>
  <tr>
    <td>JavaScript</td>
    <td>
      <ul>
        <li>Widely Used</li>
        <li>Large and rapidly growing community</li>
        <li>Variety of applications and uses (node)</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>Is not covered in the textbook</li>
        <li>Is not as flexible as Io</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>Io</td>
    <td>
      <ul>
        <li>Extremely flexible, light weight syntax</li>
        <li>Elegant implementations of coroutines, futures, and actors</li>
        <li>Powerful reflection features</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>Small community</li>
        <li>Little syntactical sugar</li>
        <li>More of a niche language</li>
      </ul>
    </td>
  </tr>
</table>
