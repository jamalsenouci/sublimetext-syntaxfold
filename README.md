#SyntaxFold - Sublime Text Plugin

A plugin for [Sublime Text][st] 3 that folds code blocks based on syntax rather than indent.

<i>Note: This does not create the folding markers as the functionality for creating that is not exposed within the sublime text api but this plugin allows us to fold based on keyboard shortcuts and the command panel.</i>

## Background
This plugin was created for a language that uses named regions similar to languages like VB, C++ and C# (see [here][vs]). Where possible use a plugin created specifically for your syntax.

## Installation
* Use [Sublime Package Control](http://wbond.net/sublime_packages/package_control "Sublime Package Control")
* `ctrl+shift+p` then select `Package Control: Install Package`
* Install SyntaxFold

Alternatively Clone this repository to your Sublime Text packages directory

### Setup
The settings file can be accessed through `Preferences -> Package Settings -> Settings - User`.  It will be initial populated with the following settings.

```json
{
    "config":[
        {
            "scope": "source.java",
            "startMarker": "//region",
            "endMarker":"//endregion"
        },
        {
            "scope": "source.cs",
            "startMarker":"#region",
            "endMarker":"#endregion"
        },
        {
            "scope": "source.c++",
            "startMarker":"#pragma region",
            "endMarker":"#pragma endregion"
        }
    ]
}
```

Add or remove fold region objects to meet your needs.  Note the `scope` key. Utilize this key to filter which source file types for which the start and end markers are active. To determine the scope name for a file type use `Tools -> Developer -> Show Scope Name'.

The `scope` key can contain a comma seperated list of scopes for which the markers should be active.  For exmaple:

```json
.
.
.
  {
    "scope": "source.c++, source.c",
    "startMarker": "#pragma region",
    "endMarker": "#pragma endregion"
  }
```
These fold markers would be active for c++ and c source files.


## Usage
Use the [keybindings](#command-examples) to fold/unfold your code

### Key Bindings ###

The following is an excerpt of the default key bindings:

```js
[
//Fold all code blocks
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
]

```

### Command Reference

A list of commands have been added to the command palette and can be accessed using `Ctrl+Shift+P`.
all commands start with "SyntaxFold : command name"

***Fold All***
Fold all code blocks in the current document

***Unfold all***
Fold all code blocks in the current document

***Fold Current***
Folds code block that cursor is in

***Unfold Current***
Unfolds code block that cursor is in

***Open README***
Open this readme file.


<!-- Links -->
[vs]:http://blogs.msdn.com/b/zainnab/archive/2013/07/12/visual-studio-2013-organize-your-code-with-named-regions.aspx
[st]: http://sublimetext.com/
