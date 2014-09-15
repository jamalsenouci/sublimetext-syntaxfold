#SyntaxFold - Sublime Text Plugin

A plugin for [Sublime Text][st] 3 that folds code based on syntax rather than indent

##Installation
Clone this repository to your Sublime Text packages directory

<!-- Links -->

[st]: http://sublimetext.com/

###Setup
On first use open the quick panel <kbd>shift</kbd>+<kbd>F5</kbd> once to set any custom fold markers and again to set your default marker.

## Usage
Use the [keybindings](#command-examples) to fold/unfold your code

### Screenshot

[![][scr-panel-thumb]][scr-panel]

### Command Examples ###

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

[st]: http://sublimetext.com/
[scr-panel]: http://i.imgur.com/wY7RlyI.jpg
[scr-panel-thumb]: http://i.imgur.com/wY7RlyI.jpg

