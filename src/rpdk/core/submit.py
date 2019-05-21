"""This sub command uploads the resource type to CloudFormation.

Projects can be created via the 'init' sub command.
"""
import logging

from .project import Project

LOG = logging.getLogger(__name__)


def submit(args):
    project = Project()
    project.load()
    project.submit(args.dry_run, args.endpoint_url, args.region)


def setup_subparser(subparsers, parents):
    # see docstring of this file
    parser = subparsers.add_parser("submit", description=__doc__, parents=parents)
    parser.set_defaults(command=submit)

    parser.add_argument(
        "--dry-run", action="store_true", help="Package the project, but do not submit."
    )

    parser.add_argument("--endpoint-url", help="CloudFormation endpoint to use.")

    parser.add_argument("--region", help="AWS Region to submit the resource type.")