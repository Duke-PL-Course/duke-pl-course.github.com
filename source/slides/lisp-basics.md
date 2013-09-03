---
layout: slide

---

<section>

# Programming Languages
### Lisp Basics

<small>Jim Posen - ECE/CS 2014</small>

</section>

<section>

# Data types
- Atoms
- Lists

</section>
<section>

## Atoms
Numbers, booleans, symbols, characters, strings

    1
    2.0
    #t
    abc
    #\a
    "hello"

</section>
<section>

## Lists
A series of elements surrounded by parenthesis

    (a b c "easy as" 1 2 3)

</section>
<section>

An element of a list is an S-expression

</section>
<section>
  <section>
## S-expressions
An S-expression is just an atom or a list

  </section>
  <section>

*Everything* in LISP is an S-expression

    (i s n t (t h i s) (c () () l?))

  </section>
  <section>
Yes, even code is made of S-expressions

    (define (factorial n)
      (if (zero? n)
          1
          (* n (factorial (- n 1)))))
  </section>
</section>
<section>
## Lists revisited
- LISP uses linked lists made of conses
- A list is either **null** or a **cons**

</section>
<section>
  <section>

## Cons
- A **cons** is just a pair of fields

  </section>
  <section>

### Simple cons
![Simple cons](http://cs.gmu.edu/~sean/lisp/cons/xb.GIF)

    (setf x (cons 'b nil))

  </section>
  <section>

### Two element list
![Two element list](http://cs.gmu.edu/~sean/lisp/cons/xab.GIF)

    (setf x (cons 'a (cons 'b nil)))

  </section>
  <section>

### Nested list
![Nested list](http://cs.gmu.edu/~sean/lisp/cons/xartb.GIF)

    (setf x '(a (r t) b))

  </section>
</section>
<section>

# Program Structure and Evaluation

</section>
<section>
  <section>

## Evaluation
- Lisp programs are made of S-expressions
- `eval` interprets and evaluates an S-expression
- The top level is called the <strong>R</strong>ead <strong>E</strong>val <strong>P</strong>rint <strong>L</strong>oop or **REPL**

  </section>
  <section>

    (eval '(+ 1 2 3))  ;; 6
    (eval '(a b c))    ;; Crash -- a is undefined

  </section>
</section>
<section>
  <section>

## Function application
- Lisp uses **prefix notation**
- The first element of an evaluated list is the function
- foo(1, 2, 3) -> (foo 1 2 3)
- 1 + 2 + 3 -> (+ 1 2 3)

  </section>
  <section>

    (+ 1 2 3)     ;; 6
    (- 1 2 3)     ;; -4
    (* (+ 1 2) (- 5 3)) ;; 6

  </section>
</section>
<section>

## Argument evalution
- Arguments are evaluated in order (usually)

</section>
<section>
  <section>

## `quote`
How to prevent evaluation of an expression?

    (setf x (a b c))  ;; CRASH -- a is undefined
  </section>
  <section>

    (setf x (quote (a b c)))  ;; Aha, much better

  </section>
  <section>

- `quote` does not evaluate its argument
- `quote` is a primitive

  </section>
  <section>

Single quotes are a shorthand for `quote`

    (setf x '(a b c))  ;; Even better yet

  </section>
</section>
<section>

# Exercises with numbers

</section>
<section>

# Primitive List Operations
- `car`
- `cdr`
- `cons`

</section>
<section>

## `car`
Returns the first element of the cons

    (car '(a b c))          ;; 'a
    (car '((a b c) d e f))  ;; '(a b c)
    (car '())               ;; Oh noes -- CRASH

</section>
<section>

## `cdr`
Returns the second element of the cons
Often the remainer of the list without the first element

    (cdr '(a b c))          ;; '(b c)
    (cdr '((a b c) d e f))  ;; '(d e f)
    (cdr '((a b c)))        ;; '()
    (cdr '())               ;; Oh noes -- CRASH

</section>
<section>

## `cons`
Creates a new cons

    (cons 'a '())                ;; '(a)
    (cons 'a '(b))               ;; '(a b)
    (cons '(a b) (cons 'c '()))  ;; '((a b) c)
    (cons 'a 'b)                 ;; '(a . b)

</section>
