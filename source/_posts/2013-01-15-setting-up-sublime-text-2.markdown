---
layout: post
title: "Setting Up Sublime Text 2"
date: 2013-01-15 02:44
comments: true
categories: intro, guide, sublime text 2
---

## Intro

![Sublime Text 2 Logo](/images/st2.jpg)

Sublime Text 2 is an incredibly fast and powerful editor that's been replacing [vim](http://en.wikipedia.org/wiki/Vim_(text_editor)), [emacs](http://en.wikipedia.org/wiki/Emacs), and [textmate](http://macromates.com/) for many. The community and ecosystem is passionate and vibrant, with developers writing packages for nearly everything. It's also freely available for all three major platforms, which makes it ideal for this class. You can download Sublime Text 2 from its [website](http://www.sublimetext.com/).

## Package Control

Sublime Text 2 supports Textmate Snippets, Syntax Highlighting, and other packages that made Textmate successful. However, Sublime Text 2 did not include a package manager out of the box. Developer [@wbond](http://wbond.net/) has creaded [a full-featured package manager][package-control] that helps discovering, installing, updating and removing packages for Sublime Text 2.

To install [Package Control][package-control], open up Sublime Text 2, and hit `ctrl+\`` or click on ***View > Show Console*** to open up the Console. Once open, paste in the following command:

```python
import urllib2,os; pf='Package Control.sublime-package'; ipp=sublime.installed_packages_path(); os.makedirs(ipp) if not os.path.exists(ipp) else None; urllib2.install_opener(urllib2.build_opener(urllib2.ProxyHandler())); open(os.path.join(ipp,pf),'wb').write(urllib2.urlopen('http://sublime.wbond.net/'+pf.replace(' ','%20')).read()); print 'Please restart Sublime Text to finish installation'
```

![Console](/images/console.png)

After it completes, you should restart Sublime Text 2 and start using Package Control. For more detailed instructions on installation, see the [Package Control Installation Guide](http://wbond.net/sublime_packages/package_control/installation).

You can access all the Package Control Commands with Sublime Text's Command Palette, which you can bring up with `Control+Shift+P` or `Command+Shift+P` on Mac.

![Command Palette](/images/command-palette.png)

A detailed description of each command can be found [here](http://wbond.net/sublime_packages/package_control/usage).

## Packages

Sublime Text natively supports JavaScript, Ruby, Scala, Erlang, Clojure, and Haskell.

### Prolog

For Prolog, a syntax highlighting package has been created by [@alnkpa](https://github.com/alnkpa/sublimeprolog). It can be installed by using *Install Package* from the *Command Palette*, which will bring up a separate window that lists all the available packages after a few seconds. Type in *Prolog* in the search and you should be able to see the package after a few key strokes. Select the *Prolog* package and press enter to install. Then that's it. Sublime Text will recognize files that with the extensions `pl` or `pro` as Prolog source files. However, `pl` is commonly used as an extension for Perl and Sublime Text will select Perl as in the languge instead of Prolog if you use a `pl` extension. As a result, we prefer to use `pro`.

![Prolog Package](/images/prolog-package.png)

As a side note, you can set the syntax of any source file at any time by using *Command Palette* > *Set Syntax: (Language)* to set the syntax of the current file to the language of your choice.

### Io

A package for Io has actualy been created by one of the instructors [@yangsu](https://github.com/yangsu/sublime-io). However, it has yet to be approved. As a result, some additional steps need to be taken.

First, bring up *Package Control Settings* by typing *Preferences: Package Control Settings - User* and press enter to open it up.

![Package Control Preferences](/images/package-control-prefs.png)

Once open, scroll to the bottom of the file to the `repository_channels` field. Add in the following link to the list. Don't forget the comma delimiter.
```
"https://raw.github.com/wbond/package_control_channel/master/repositories.json"
```

![Package Control Preferences repository_channels](/images/package-control-prefs-repo.png)

Now, bring up *Install Package* again and search for `sublime-io` and install it like any other package. 

![sublime-io](/images/package-control-prefs-io.png)

After the installation completes, Sublime Text will recognize any file with `io` extention as `io` source files. As noted above, you can also set the syntax of any source file to io with *Command Palette* > *Set Syntax: (Language)*.

### Additional Resources

[Tuts+][tuts] is an amazing collection of resources for almost everything related to technical or design knowledge. It's highly recommended for anyone trying to learn anything from Photoshop to [Node.js](http://nodejs.org/). [Tuts+][tuts] also has a whole network of sites with focuses in particular areas. Scroll to the bottom of the [Tuts+ page][tuts], and you will be able to see all the available options.

[NetTuts+](http://net.tutsplus.com/tutorials/) in particular has many great tutorials on Sublime Text. Two of the best articles are [Sublime Text 2 Tips and Tricks](http://net.tutsplus.com/tutorials/tools-and-tips/sublime-text-2-tips-and-tricks/) and [Essential Sublime Text 2 Plugins and Extensions](http://net.tutsplus.com/tutorials/tools-and-tips/essential-sublime-text-2-plugins-and-extensions/).

You can also follow [a free video series](https://tutsplus.com/course/improve-workflow-in-sublime-text-2/) by Jeffrey Way on [Tuts+][tuts] that goes over many of the topics covered in the two articles above and more.

[tuts]: https://tutsplus.com/
[package-control]: http://wbond.net/sublime_packages/package_control