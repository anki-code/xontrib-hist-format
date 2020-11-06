def _hist_format(args):
    import argparse, os

    argp = argparse.ArgumentParser(prog='hist-format', description="Format xonsh history to post it to Github or another page.")
    argp.add_argument('-f', '--format', default='md', help="Format: md, txt.")
    argp.add_argument('-c', '--commands-count', default=10, help="Count of commands")
    argp.add_argument('-l', '--commands-list', action='store_true', help="Show commands in distinct section.")
    argp.add_argument('-H', '--output-head-count', nargs='?', const=10, help="Count of lines from output head to show.")
    argp.add_argument('-T', '--output-tail-count', nargs='?', const=10, help="Count of lines from output tail to show.")
    argp.add_argument('-m', '--min', action='store_true', help="Make block minimized i.e. by adding <details> tag in Markdown.")
    argp.add_argument('--lines', action='store_true', help="Add additional lines before and after.")
    opt = argp.parse_args(args)

    opt.commands_count = abs(int(opt.commands_count))
    if opt.output_head:
        opt.output_head = abs(int(opt.output_head))
    if opt.output_tail:
        opt.output_tail = abs(int(opt.output_tail))

    formats = {
        'md': {'begin': '```python', 'end': '```', 'comment': '# '},
        'txt': {'begin': '', 'end': '', 'comment': '# '}
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
    for i in list(range(len(__xonsh__.history) - 1, -1, -1)):
        h = __xonsh__.history[i]
        if 'hist-format' in h.cmd or 'hist-md' in h.cmd or 'hist-txt' in h.cmd:
            continue
        if len(cmds_idx) >= opt.commands_count or h.cmd.rstrip() == 'clear':
            break
        cmds_idx.append(i)

    if opt.min:
        if opt.format == 'md':
            print()
            print('<details>')

    if opt.lines:
        print()
        print('-' * term_cols)

    if opt.format == 'md':
        print('\nOutput:\n')
    else:
        print('\nOutput:\n')

    print(format['begin'])
    for i in cmds_idx[::-1]:
        h = __xonsh__.history[i]
        print(h.cmd.rstrip(), end='')
        if h.out:
            print()
            output_lines = [format['comment'] + l for l in str(h.out).rstrip().split('\n')]

            if opt.output_head and opt.output_tail:
                if (opt.output_head + opt.output_tail) < len(output_lines):
                    print('\n'.join(output_lines[:opt.output_head]))
                    print(format['comment'])
                    print(format['comment'] + f'---- Skipped {len(output_lines) - opt.output_head - opt.output_tail} lines of output ----')
                    print(format['comment'])
                    print('\n'.join(output_lines[-opt.output_tail:]))
                else:
                    print('\n'.join(output_lines))

            elif opt.output_head:
                print('\n'.join(output_lines[:opt.output_head]))
                skipped = len(output_lines) - opt.output_head
                if skipped > 0:
                    print(format['comment'] + f'---- Skipped next {skipped} lines of output ----')
            elif opt.output_tail:
                skipped = len(output_lines) - opt.output_tail
                if skipped > 0:
                    print(format['comment'] + f'---- Skipped prev {skipped} lines of output ----')
                print('\n'.join(output_lines[-opt.output_tail:]))
            else:
                print('\n'.join(output_lines))

        print()
        cmds.append(h.cmd.rstrip())
    print(format['comment'] + 'Prepared by xontrib-hist-format')
    print(format['end'])

    if opt.commands_list:
        if opt.format == 'md':
            print('\nCommands:\n')
        else:
            print('\nCommands:\n')

        print(format['begin'])
        for c in cmds:
            print(c)
        print()
        print(format['comment'] + 'Prepared by xontrib-hist-format')
        print(format['end'])

    if opt.lines:
        print()
        print('-' * term_cols)

    if opt.min:
        if opt.format == 'md':
            print()
            print('</details>')

aliases['hist-format'] = _hist_format
aliases['hist-md'] = ['hist-format', '-f', 'md']
aliases['hist-txt'] = ['hist-format', '-f', 'txt']
del _hist_format
