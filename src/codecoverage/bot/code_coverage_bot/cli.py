# -*- coding: utf-8 -*-
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import click

from cli_common.cli import taskcluster_options
from cli_common.log import init_logger
from shipit_code_coverage import config
from shipit_code_coverage.codecov import CodeCov
from shipit_code_coverage.secrets import secrets


@click.command()
@taskcluster_options
@click.option('--revision', envvar='REVISION')
@click.option(
    '--cache-root',
    required=True,
    help='Cache root, used to pull changesets'
)
def main(revision,
         cache_root,
         taskcluster_secret,
         taskcluster_client_id,
         taskcluster_access_token,
         ):
    secrets.load(taskcluster_secret, taskcluster_client_id, taskcluster_access_token)

    init_logger(config.PROJECT_NAME,
                PAPERTRAIL_HOST=secrets.get('PAPERTRAIL_HOST'),
                PAPERTRAIL_PORT=secrets.get('PAPERTRAIL_PORT'),
                SENTRY_DSN=secrets.get('SENTRY_DSN'),
                MOZDEF=secrets.get('MOZDEF'),
                )

    c = CodeCov(revision, cache_root, taskcluster_client_id, taskcluster_access_token)
    c.go()


if __name__ == '__main__':
    main()
