def get_offsets(tk_window):
    """
        Returns an appropriate offset for a given tkinter toplevel,
        such that it always shows center screen on the primary display.
    """

    width_offset = int(
        (tk_window.winfo_screenwidth() / 2) - (tk_window.winfo_width() / 2)
    )

    height_offset = int(
        (tk_window.winfo_screenheight() / 2) - (tk_window.winfo_height() / 2)
    )

    return (width_offset, height_offset)


def set_offsets(tk_window, offsets):
    """Set geometry offsets on a given Tk window"""

    tk_window.geometry(
        f"+{offsets[0]}+{offsets[1]}"
    )
    tk_window.update()
