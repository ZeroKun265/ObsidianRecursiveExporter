# ObsidianRecursiveExporter
A way to export all notes linked to one main note in an obsidian vault inspired by klalle/ObsidianToHtmlConverter

Currently not functional, will update once a Minimum Viable Product is ready for deployment
## What currently works:
- Identifying the links in a file (currently just the main file)

## What needs to work for an MVP
- Recursively look for links in all linked files
- Generate a folder and file structure equal to that of the vault
- Generate temporary files where links are replaced with their ids
- Generate either Markdown or HTML from the temporary files in the same structure

###### Note: For an MVP images are the only attachment that i will focus on, see below 

## Features i'd like to add
- Handling of excalidraw and pdf attachments
- Import of obsidian style and settings into Markdown export
- Link depth limiter, to add only notes that are close to the main file by a certain amount of steps

## Features i'd like to add but seem very hard
- HTML export with equal css style to that of the obsidian vault
- Handling of Folder Icon bbcards syntax
