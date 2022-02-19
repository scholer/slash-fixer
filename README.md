# slash-fixer
Small command line tool to convert forward slashes to backward slashes. Because Windows just had to be different.

### Installation:

```
pip install git+https://github.com/scholer/slash-fixer.git
```


### Examples:

```

# By default, if input path contains forward slashes, all slashes are converted to backslashes:
$> fix-slashes input/path/containing/forward/slashes
input\path\containing\forward\slashes

# If input path does not contain any forward slashes, all backslashes are converted to forward slashes:
$> fix-slashes input\path\containing\backward\slashes
input/path/containing/backward/slashes


# You can use either 'fix-slashes' or 'slash-fixer' commands (identical entry points):
$> slash-fixer input/path/containing/forward/slashes


# Using the python module instead of the entry point:
$> python -m slash_fixer input/path/containing/forward/slashes

```


### TODO:

* Add support for saving output to clipboard. Because `fix-slashes input\path\containing\backward\slashes | clip`  (or `xclip`) is just too hard to remember.

