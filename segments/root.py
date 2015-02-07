def add_root_indicator_segment():
    root_indicators = {
        'bash': ' \\$ ',
        'zsh': ' \\$ ',
        'bare': ' $ ',
    }
    bg = Color.CMD_PASSED_BG
    fg = Color.CMD_PASSED_FG
    extra = ""
    if powerline.args.prev_error != 0:
        fg = Color.CMD_FAILED_FG
        bg = Color.CMD_FAILED_BG
        extra = " %d" % (powerline.args.prev_error)
    text = extra + root_indicators[powerline.args.shell]
    powerline.append(text, fg, bg)

add_root_indicator_segment()
