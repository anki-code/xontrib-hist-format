def _hist_format(args):
    import argparse, os

    argp = argparse.ArgumentParser(prog='hist-format', description="Format xonsh history")
    argp.add_argument('-f', '--format', default='md', help="Format: md.")
    argp.add_argument('-c', '--count', default=10, help="Count of commands")
    argp.add_argument('-l', '--lines', action='store_true', help="Add additional lines before and after.")
    opt = argp.parse_args(args)

    opt.count = int(opt.count)

    formats = {
        'md': {'begin': '```python', 'end': '```', 'comment': '#'}
    }
    format = formats[opt.format]

    if opt.lines:
        try:
            ts = os.get_terminal_size()
            term_cols = ts.columns
        except Exception:
            term_cols = 10

    cmds = []
    cmds_idx = []
    for i in list(range(len(__xonsh__.history) - 1, 0, -1)):
        h = __xonsh__.history[i]
        if 'hist-format' in h.cmd or 'hist-md' in h.cmd:
            continue
        if len(cmds_idx) >= opt.count or h.cmd.rstrip() == 'clear':
            break
        cmds_idx.append(i)

    if opt.lines:
        print()
        print('-' * term_cols)
    print('\n<sub>[hist-format](https://github.com/anki-code/xontrib-hist-format) output:</sub>\n')
    print(format['begin'])

    for i in cmds_idx[::-1]:
        h = __xonsh__.history[i]
        print(h.cmd.rstrip(), end='')
        if h.out:
            print()
            print('\n'.join([format['comment'] + l for l in str(h.out).rstrip().split('\n')]))
        print()
        cmds.append(h.cmd.rstrip())
    print(format['end'])

    print('\n<sub>[hist-format](https://github.com/anki-code/xontrib-hist-format) command:</sub>\n')
    print(format['begin'])
    for c in cmds:
        print(c)
    print(format['end'])

    if opt.lines:
        print()
        print('-' * term_cols)


aliases['hist-format'] = _hist_format
aliases['hist-md'] = ['hist-format', '-f', 'md']
del _hist_format