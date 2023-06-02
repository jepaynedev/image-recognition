"""Console script to automate some dataset functionality

Scripted aquisition and project setup for ease of use and reproducibility
"""
import argparse
import logging


logging.basicConfig(
    level=logging.INFO,
    format='%(message)s',
    handlers=[logging.StreamHandler()],
)
logger = logging.getLogger(__name__)


# Console arguments metadata and help
NAME = "dataset"
DESCRIPTION = "Download, extraction, and organization of known datasets"
# Script constants
DATASETS_DIRNAME = ".datasets"


def parse_arguments(args=None):
    """Parse command line arguments for the datasets script"""
    parser = argparse.ArgumentParser(
        prog=NAME,
        description=DESCRIPTION,
    )
    parser.add_argument(
        "command",
        choices=["install"],
        help="Dataset command to execute",
    )
    parser.add_argument(
        "--log-level", "-l",
        choices=[
            'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'
        ],
        default='INFO',
        help="Set the logging level",
    )
    parser.add_argument(
        "--force", "-f",
        action="store_true",
        help="Force reinstallation of the dataset if it already is installed",
    )
    return parser.parse_args(args)


def main():
    """Entry point for dataset console script"""
    args = parse_arguments()
    logger.setLevel(logging.getLevelName(args.log_level))
    logger.debug(args)


if __name__ == '__main__':
    main()
