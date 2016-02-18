# sublime-plantuml

## What it does

When you save a `.uml` file a event listener runs a command
that calls to a PlantUML process that will save a `.png` file next to your `.uml` file.
Then a new view is opened with the UML png rendered.

## Quick start guide

Browse to your Sublime Text 3 packages directory

```
cd ~/.config/sublime-text-3/Packages
git clone git@github.com:pkucmus/sublime-plantuml.git PlantUML
```

It uses docker (configuration awareness to change the plantuml executable contribution welcome)

```
cd ~/.config/sublime-text-3/Packages/PlantUML
docker build -t plantuml .
```
Restart Sublime you should be ready to go.
