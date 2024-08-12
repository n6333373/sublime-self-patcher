## Sublime Self Patcher

This is a Sublime Text 4 plugin which can patch Sublime Text itself (and Sublime Merge).

🔥 No third-party dependency is required. The only thing needed is Sublime Text itself.

## Supported Environments

- Linux x64
- Windows x32
- Windows x64

There is no other platform or architecture supported because I don't use them.

## Download

https://github.com/n6333373/sublime-self-patcher/archive/refs/heads/main.zip

## Installation

First, you have to find out the `Packages` directory.

- If you are using a portable version of Sublime Text, it is `Data/Packages`.
- If you are using an installed version of Sublime Text,
  - On Windows, it is `%appdata%\Sublime Text\Packages`.
  - On Linux, it is `$HOME/.config/sublime_text/Packages`.

Now, (decompress if necessary) put the downloaded directory into the `Packages` directory
so that the directory structure looks like the following:

```text
Packages/
└── SelfPatcher/
    ├── boot.py
    ├── ...
```

## Usage

### Patch Self (The Current Sublime Text)

- If you are using a unregistered dev build, this plugin should show a popup for patching when starting.
- If you are using a stable build, you can patch from the menu: `Help ⇒ Patch This Application`

### Patch External Sublime Text/Merge

Click the menu: `Help ⇒ Patch External Sublime Text/Merge` and then select the executable of Sublime Text/Merge.

## Q&A

### How to Disable Sublime Text/Merge Auto Update?

This plugin usually just continues to work for future versions of Sublime Text/Merge.
But if you want to disable the application auto update, you can set the following settings:

```json
{
    "update_check": false
}
```

### This Plugin is Suspicious

I don't think I do anything malicious, but if you don't trust me, you can always do it by yourself.
See https://gist.github.com/maboloshi/feaa63c35f4c2baab24c9aaf9b3f4e47
