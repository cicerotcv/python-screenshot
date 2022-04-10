import argparse


def get_context():
    parser = argparse.ArgumentParser("asdf")
    parser.add_argument("--context", type=str, default='')
    args = parser.parse_args()
    context = args.context
    return context
