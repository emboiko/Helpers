from win32api import SetCursorPos, GetSystemMetrics

#for when the cursor gets lost in your 10 displays
#firstworldproblems 
#bind me to your mmo mouse / key combo, etc

def reset_mouse():
    SetCursorPos(
        (
            int(GetSystemMetrics(0) / 2),
            int(GetSystemMetrics(1) / 2)
        )
    )


def main():
    reset_mouse()


if __name__ == "__main__":
    main()
