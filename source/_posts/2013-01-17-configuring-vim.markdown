---
layout: post
title: "Configuring Vim"
date: 2013-01-17 15:55
comments: true
categories: intro, guide, vim
---

## Installing Vim

Most Unix-like systems like Mac OS X or Linux distributions will come with Vim installed already. However, you may want to upgrade vim for better compatability or new features. Here, we will cover some of the recommended ways to install `vim`.

### OS X Installation

One option to install Vim for OS X is to use [MacVim](http://code.google.com/p/macvim/), a GUI version of vim. Simply download and install MacVim from its project page's [Downloads](http://code.google.com/p/macvim/downloads/list) tab. Installation just requires unarchiving the `.tbz` file (Archive Utility should be able to do this for you by double clicking on the archive). Finally, drag and drop the `MacVim.app` bundle into your `/Applications/` folder.

Alternatively, you can use [`brew`](http://mxcl.github.com/homebrew/) to install MacVim. If you prefer a terminal-based vim, than you can run the following commands with `brew`:

```bash
brew install vim --with-python --with-ruby --with-perl --with-lua --with-tcl
```

### Windows Installation

You can download the latest version of vim directly from the [vim webpage](http://www.vim.org/download.php#pc). This includes the binaries for the 32-bit and 64-bit version of Windows.

Alternatively, you can install a command-line version of vim through [Cygwin](http://www.cygwin.com/), a Unix-like environment and CLI for Windows. First [install Cygwin](http://cygwin.com/install.html) by downloading the `setup.exe` file. Run the `setup.exe` file with your preferred installation settings. Once reaching the "Select Packages" screen, scroll down to the **Editors** node and expand it. Finally, find **vim** in the list and change the *Skip* option to *Install*.


## TO BE CONTINUED...
