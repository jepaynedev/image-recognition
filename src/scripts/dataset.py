"""Console script to automate some dataset functionality

Scripted aquisition and project setup for ease of use and reproducibility
"""
import argparse
import logging
import pathlib


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


def get_project_dir():
    """Resolves the project root directory relative to the current file"""
    parent_dir = pathlib.Path(__file__).parent
    while parent_dir.name != 'src':
        parent_dir = parent_dir.parent
    # Parent of src folder is the project root directory
    project_dir = parent_dir.parent
    return project_dir


def get_datsets_dir(ensure_exists=False):
    """Resolves the standard directory for datasets and optionally create if necessary"""
    project_dir = get_project_dir()
    datasets_dir = project_dir / DATASETS_DIRNAME
    if ensure_exists:
        datasets_dir.mkdir(parents=True, exist_ok=True)
    return datasets_dir


def main():
    """Entry point for dataset console script"""
    args = parse_arguments()
    logger.setLevel(logging.getLevelName(args.log_level))
    logger.debug(args)


if __name__ == '__main__':
    main()
