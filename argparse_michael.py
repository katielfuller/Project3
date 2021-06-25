def formatter(prog):
    return argparse.HelpFormatter(prog, max_help_position=100, width=200)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = "This shows current Covid cases and Covid deaths in Texas and Texas counties")

