#SyntaxFold - Sublime Text Plugin

A plugin for [Sublime Text][st] 3 that folds code blocks based on syntax rather than indent.  

##Background
This plugin was created for a language that uses named regions similar to languages like VB, C++ and C# (see [here][vs]). Where possible use a plugin created specifically for your syntax.

##Installation
* Use [Sublime Package Control](http://wbond.net/sublime_packages/package_control "Sublime Package Control")
* `ctrl+shift+p` then select `Package Control: Install Package`
* Install SyntaxFold

Alternatively Clone this repository to your Sublime Text packages directory


###Setup
* On first use open the quick panel <kbd>shift</kbd>+<kbd>F5</kbd> 

![][add-another]
* select add another to set any custom fold markers. If your markers contain special characters then escape them by preceding them with a /.

![][custom-fold]
* open the quick panel <kbd>shift</kbd>+<kbd>F5</kbd> again to set your default marker


* You can specify start and end markers, or if you just specify the start marker then it will fold up to the next start marker.

![][scr-panel-thumb]


## Usage
Use the [keybindings](#command-examples) to fold/unfold your code

### Key Bindings ###

The following is an excerpt of the default key bindings:

```js
[
// Fold all code blocks
  { "keys": ["alt+0", "alt+0"],
    "command": "fold_all" },

// Unfold all code blocks
  { "keys": ["alt+shift+0", "alt+shift+0"],
    "command": "unfold_all"},

// Fold current code blocks
  { "keys": ["alt+1", "alt+1"],
    "command": "fold_current"},

// Unfold current code blocks
  { "keys": ["alt+shift+1", "alt+shift+1"],
    "command": "unfold_current"},

// Open quick panel to change default language
  { "keys": ["shift+f5"],
    "command": "fold_panel"}
]

```

### Command Reference

A list of commands have been added to the command palette and can be accessed using `Ctrl+Shift+P`.
all commands start with "SyntaxFold : command name"

***fold_panel***

Open a quick panel to set default language and specify custom fold markers


***fold_all***
Fold all code blocks in the current document

***unfold_all***
Fold all code blocks in the current document

***fold_current***
Folds code block that cursor is in

***unfold_current***
Unfolds code block that cursor is in


<!-- Links -->
[vs]:http://blogs.msdn.com/b/zainnab/archive/2013/07/12/visual-studio-2013-organize-your-code-with-named-regions.aspx
[st]: http://sublimetext.com/
[scr-panel]: http://i.imgur.com/wY7RlyI.jpg
[scr-panel-thumb]: http://i.imgur.com/wY7RlyI.jpg
[custom-fold]: http://i.imgur.com/7bxfhkO.jpg
[add-another]: http://i.imgur.com/qNBUUbI.jpg
