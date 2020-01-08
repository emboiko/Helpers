from re import match

def rgb_to_hex(rgb:tuple):
    """
        RGB tuple (no alpha) => Hex color notation
    """

    if type(rgb) is not tuple:
        raise TypeError("Argument must be of type 3-Tuple.")

    for i in range(len(rgb)):
        if type(rgb[i]) is not int:
            raise TypeError("Input must be a 3-tuple of integers in range 0-255 (0,0,0)")
        if i >= 3:
            raise IndexError("Input must be a 3-tuple of integers in range 0-255 (0,0,0)")
        if rgb[i] < 0 or rgb[i] > 255:
            raise ValueError("Input must be a 3-tuple of integers in range 0-255 (0,0,0)")

    return f"#{rgb[0]:02X}{rgb[1]:02X}{rgb[2]:02X}"


def hex_to_rgb(hex_:str):
    """
        Hex color notation => RGB Tuple (no alpha)
    """
    
    if type(hex_) is not str:
        raise TypeError("Argument must be of type String.")
    if not hex_.startswith("#"):
        raise ValueError("Notation must contain an octothorpe(#) at index 0. (#FFFFFF)")
    if len(hex_) >= 8 or len(hex_) <= 6:
        raise IndexError("Notation must contain exactly 7 characters. (#FFFFFF)")
    if not match("#([A-F]|\d){6}", hex_):
        raise ValueError(f"Invalid input: {hex_}")

    return tuple([int(hex_[i] + hex_[i+1],16) for i in range(len((hex_))) if i % 2 != 0])
    

def main():
    assert("#000000" == rgb_to_hex((0,0,0)))
    assert("#FFFFFF" == rgb_to_hex((255,255,255)))
    assert("#A2F1F7" == rgb_to_hex((162, 241, 247)))
    assert((0,0,0) == hex_to_rgb(("#000000")))
    assert((255,255, 255) == hex_to_rgb(("#FFFFFF")))
    assert((162, 241, 247) == hex_to_rgb(("#A2F1F7")))


if __name__ == "__main__":
    main()