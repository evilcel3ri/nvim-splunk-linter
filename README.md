# Nvim Splunk Linter

This plugin will lint your Splunk search. It is quite very experimental for now.

## Install

You need Python in your PATH or in your Nvim config:

```
let g:python3_host_prog = '/usr/bin/python3'
let g:python_host_prog = '/usr/bin/python2'
```

Add the plugin to your plugin manager (here with [vim-plug](https://github.com/junegunn/vim-plug)):

```
Plug 'christalib/nvim-splunk-linter'
```

Run:

```
:PlugInstall
:UpdateRemotePlugins
```

## Use

There is a for the moment one function that will ident your Splunk query but
will keep the first line (I know, I'll fix it as soon as I figure the API out).

```
:call LintSplunk()
```

```
test (on) (one) (one (two (three))) (one) ((two))

# to

test
	(on)
	(one)
	(one
		(two
			(three)))
(one)
(
	(two))
```

## Contribute

You're very welcome. It's my first plugin.
