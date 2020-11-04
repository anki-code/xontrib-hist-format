<p align="center">
Format xonsh history to post it to Github or another page.
</p>

<p align="center">  
If you like the idea click ⭐ on the repo and stay tuned.
</p>


## Installation

To install use pip:

```bash
xpip install xontrib-hist-format
# or: xpip install -U git+https://github.com/anki-code/xontrib-hist-format
```

## Usage

```bash
xontrib load hist_format
hist-format --help         # Basic command
hist-md                    # Markdown (md) shortcut
```
```
usage: hist-format [-h] [-f FORMAT] [-c COUNT] [-l]

optional arguments:
  -h, --help            show this help message and exit
  -f FORMAT, --format FORMAT
                        Format: md.
  -c COUNT, --count COUNT
                        Count of commands
  -l, --lines           Add additional lines before and after.
```

## Example
Run commands:
```python
echo 123
ls / | head -n 3
```
Run hist-format:
```python
hist-md -c 2 -l    # latest 2 commands with header and footer as line
```
As result you will get the output that you can copy and paste in Github comment or md-file:

------------------------------------------------------------------------------------------------------------------

<sub>[hist-format](https://github.com/anki-code/xontrib-hist-format) output:</sub>

```python
echo 123
#123

ls / | head -n 3
#boot
#cdrom
#dev

```

<sub>[hist-format](https://github.com/anki-code/xontrib-hist-format) commands:</sub>

```python
echo 123
ls / | head -n 3
```

------------------------------------------------------------------------------------------------------------------

## Known issues

Not every command has output in the `__xonsh__.history`.

## Credits

* This package was created with [xontrib cookiecutter template](https://github.com/xonsh/xontrib-cookiecutter).
* Take a look at [ergopack](https://github.com/anki-code/xontrib-ergopack) - the pack of ergonomic xontribs.