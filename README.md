<p align="center">
Format xonsh history to post it to Github or another page.
</p>

<p align="center">
The mission of xontrib-hist-format is to make commands repeatable, copy-pastable and save time to preparing.
</p>

<p align="center">  
If you like the idea click ⭐ on the repo and stay tuned.
</p>


## Installation

```bash
xpip install xontrib-hist-format
# or: xpip install -U git+https://github.com/anki-code/xontrib-hist-format
```

## Usage

```bash
xontrib load hist_format
hist-format --help         # Basic command
hist-md                    # Markdown format shortcut
hist-txt                   # Text format shortcut
```

Arguments:
```
usage: hist-format [-h] [-f FORMAT] [-c COMMANDS_COUNT] [-l] 
                   [-H [OUTPUT_HEAD_COUNT]] [-T [OUTPUT_TAIL_COUNT]]
                   [-m] [--lines]

Format xonsh history to post it to Github or another page.

optional arguments:
  -h, --help            show this help message and exit
  -f FORMAT, --format FORMAT
                        Format: md, txt.
  -c COMMANDS_COUNT, --commands-count COMMANDS_COUNT
                        Count of commands
  -l, --commands-list   Show commands in distinct section.
  -H [OUTPUT_HEAD_COUNT], --output-head-count [OUTPUT_HEAD_COUNT]
                        Count of lines from output head to show.
  -T [OUTPUT_TAIL_COUNT], --output-tail-count [OUTPUT_TAIL_COUNT]
                        Count of lines from output tail to show.
  -m, --min             Make block minimized i.e. by adding <details> tag in Markdown.
  --lines               Add additional lines before and after.

```

Note! The `clear` command is used as marker of the beginning of commands list. If you run commands 1, 2, 3 
then run `clear`, and run 4, 5, 6 and finally run `hist-md` it will show 4, 5, 6 commands.
Feel free to open an issue with feedback on this approach.

## Example
Run commands:
```python
echo 123
ls / | head -n 3
```
Run hist-format:
```python
hist-md -c 2 -l --lines    # latest 2 commands + commands list + header and footer as line
```
As result you will get the output that you can copy and paste to the Github comment or md-file:

------------------------------------------------------------------------------------------------------------------

Output:

```python
echo 123
#123

ls / | head -n 3
#boot
#cdrom
#dev

# Prepared by xontrib-hist-format
```

Commands:

```python
echo 123
ls / | head -n 3

# Prepared by xontrib-hist-format
```

------------------------------------------------------------------------------------------------------------------

## Clipboard

You can redirect the output to clipboard. Example for [xclip](https://github.com/astrand/xclip):
```python
hist-md | xclip
```

## Known issues

Not every command has output in the `__xonsh__.history`.

## Credits

* This package is the part of [ergopack](https://github.com/anki-code/xontrib-ergopack) - the pack of ergonomic xontribs.
* This package was created with [xontrib cookiecutter template](https://github.com/xonsh/xontrib-cookiecutter).
