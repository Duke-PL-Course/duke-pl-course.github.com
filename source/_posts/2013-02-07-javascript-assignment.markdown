---
layout: post
title: "JavaScript Assignment"
date: 2013-02-07 17:29
comments: true
categories: JavaScript, Assignments
---

<img src="/images/jslogo.png" alt="JavaScript" style="max-height: 200px; float: left; margin-right: 10px;">

With our last lecture, we have finished the material for JavaScript. The slides from lecture can be found [here][slides].

The [JavaScript Assignment][assignment] is now live and complete. It includes **four** problems, with one bonus problem. The assignment will be due **next Wednesday, February 13 at 11:59PM**.

The assignment document is called [2013-02-03-assignment.md][assignment] and the skeleton files can be found under the [assignments][] folder.

Please remember to fork the [JavaScript repo][repo] and push your solutions to your forked repo. You can always manually submit to the [autograder][].

Again, please feel free to post questions on [issues][].

Hope you will find this assignment to be slightly easier.

## Note About Bonus Problem

The [waterfall function][bonus] is part of a very widely used JavaScript Library called [async.js][]. It helps manage the complexity and callbacks for a series of functions that depend on the result of a previous functions.

A similar function also available in the async library is [parallel][]. It allows you to fire off many requests in parallel and collect the results with a single callback function. We mentioned this function in lecture and we have published a simpler version of the parallel function that takes in a hash. Please take a look for reference and hopefully it will help you understand what's required for the waterfall function

## Note about Earlier Forked Repos

If you forked the repo before we finalized the assignment. Please use the following commands to update your repo:

```bash
git remote add upstream git@github.com:Duke-PL-Course/JavaScript.git
git pull --rebase upstream master
```

Let us know if you are having trouble with git.

[slides]: /slides/javascript.html
[assignment]: https://github.com/Duke-PL-Course/JavaScript/blob/master/2013-02-03-assignment.md
[assignments]: https://github.com/Duke-PL-Course/JavaScript/tree/master/assignments
[repo]: https://github.com/Duke-PL-Course/JavaScript
[autograder]: http://dukeplcourse.com
[issues]: https://github.com/Duke-PL-Course/JavaScript/issues?state=open
[parallel]: https://github.com/Duke-PL-Course/JavaScript/blob/master/assignments/bonus-parallel.js
[async.js]: https://github.com/caolan/async
[bonus]: https://github.com/Duke-PL-Course/JavaScript/blob/master/2013-02-03-assignment.md#bonus-async-waterfall
[parallel]: https://github.com/caolan/async#paralleltasks-callback