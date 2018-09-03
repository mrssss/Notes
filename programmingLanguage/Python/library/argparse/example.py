import argparse


def create_parser():
    parser = argparse.ArgumentParser(description="This is an argparse example",
                                     usage="Usage can be modified",
                                     # you can specify the formatter for print the help page
                                     # formatter_class=argparse.RawDescriptionHelpFormatter,
                                     epilog="This is the help page tail")
    return parser


def add_args(parser):
    parser.add_argument('--foo', help="foo help")


def main():
    parser = create_parser()
    add_args(parser)
    parser.parse_args()


if __name__ == "__main__":
    main()
