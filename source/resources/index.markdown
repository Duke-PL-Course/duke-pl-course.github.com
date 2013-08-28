---
layout: page
title: "Resources"
date: 2013-01-14 02:40
footer: false
---

## Table of Contents
* [Installation](#installation)
    * [Virtual Machine](#virtual-machine)
    * [Mac OS X](#mac-os-x)
    * [Windows](#windows)
    * [Linux](#linux)
* [Unix](#unix)
* [Git](#git)
* [Editors](#editors)
    * [Emacs](#emacs)
    * [Sublime Text 2](#sublime-text-2)
    * [Vim](#vim)
* [Language Specific Resources](#language-specific-resources)

* [Downloads](#downloads)

<h2 id="installation">Installation</h2>

<h3 id="virtual-machine">Virtual Machine</h3>

I have created a [Lubuntu](http://www.lubuntu.net/) virtual machine which I highly recommmend using for this class. The languages and environments are already installed and you avoid clustering your operating system with languages that you may not use again for a while. *If you do not have a lot of RAM on your computer, this may not be a good option.*

To install the virtual machine, you need virtualization software like [VirtualBox](https://www.virtualbox.org/) or VMWare, which can be downloaded for free through [Duke OIT](http://oit.duke.edu/comp-print/software/). You should be able to import the [this image](https://d164gy67scumxg.cloudfront.net/plcourse.ova) using the virtualization software. Instructions for VirtualBox are [here](http://www.virtualbox.org/manual/ch01.html#ovf).

<h3 id="mac-os-x">Mac OS X</h3>

Type this in your terminal:

```bash
curl https://gist.github.com/jimpo/6357542/raw/37c2c7a5ea99738abfb9a52d3da060af18ca397a/Duke-PL-Course-MacOSX-Install.sh | sh
```

You should be set after the script completes.

If you are interested in what the install script is doing, you can view the source [here](https://gist.github.com/jimpo/6357542).

<h3 id="windows">Windows</h3>

Since many of the languages can't run natively on Windows, I have created a Virtual Machine for you to use. Follow the above instructions to set it up.

<h3 id="linux">Linux</h3>

You can install most of the packages using `apt-get` or its equivalent for your distribution. If you are having trouble, please let the instructors know.

```bash
sudo apt-get install racket ghc swi-prolog ruby1.9.3 scala
```

<h2 id="unix">Unix</h2>

In this class, we will be working on a Linux distribution (or OSX, which is Unix based). You should be comfortable using a command line. If you don't have much experience with Unix based systems, I recommend [this tutorial](http://linuxcommand.org/lc3_learning_the_shell.php).

<h2 id="git">Git</h2>

[Pro Git](http://git-scm.com/book/) is a introduction to git.

Most problems can be found using google or stackoverflow. If you are still having trouble, let the instructors know.

### Branching
[Learn Git Branching](http://pcottle.github.com/learnGitBranching/)

<h2 id="editors">Editors</h2>

<h2 id="sublime-text-2">Sublime Text 2</h2>

We suggest that you use [Sublime Text 2](http://www.sublimetext.com/), a cross platform editor that's extremely flexible. You can download and evaluate it for free indefinitely. Follow the instructions in [this post](/blog/2013/01/15/setting-up-sublime-text-2/) to set up [Package Control](http://wbond.net/sublime_packages/package_control) and other useful packages to make your development environment easier to work with.

<h2 id="emacs">Emacs</h2>

If are willing to put some effort into learning a terminal based editor, it will pay large dividends in the future. Both emacs and vim are very powerful and highly customizable terminal based editors. The emacs environment is the provided virtual machine image is already configured for the languages we will be using.

Here is a good emacs [tutorial](http://david.rothlis.net/emacs/howtolearn.html) for those interested.

<h2 id="vim">Vim</h2>

If you are a vim user or would like to use vim for this course, then you can find the recommended plugins and configuration files in [this archive](https://www.dropbox.com/s/bka5j2rkobq0gxu/vimdotfiles.tgz). In addition, you can find a blog post on how to install and configure vim [here](/blog/2013/01/17/configuring-vim/).

<h2 id="language-specific-resources">Language Specific Resources</h2>

<h2 id="downloads">Downloads</h2>

[Shared Dropbox folder with course resources](https://www.dropbox.com/sh/i02fg0bhisrzsx0/H2o-7DuA3G)
