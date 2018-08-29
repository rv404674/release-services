# -*- coding: utf-8 -*-
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import os

import cli_common.taskcluster
import shipit_code_coverage_backend.config

secrets = cli_common.taskcluster.get_secrets(
    os.environ.get('TASKCLUSTER_SECRET'),
    shipit_code_coverage_backend.config.PROJECT_NAME,
    required=['ESFRONTLINE', 'PHABRICATOR_TOKEN'],
    existing={x: os.environ.get(x) for x in ['REDIS_URL'] if x in os.environ},
    taskcluster_client_id=os.environ.get('TASKCLUSTER_CLIENT_ID'),
    taskcluster_access_token=os.environ.get('TASKCLUSTER_ACCESS_TOKEN'),
)

REDIS_URL = secrets['REDIS_URL'] if 'REDIS_URL' in secrets else 'redis://localhost:6379'
CODECOV_ACCESS_TOKEN = secrets['CODECOV_ACCESS_TOKEN'] if 'CODECOV_ACCESS_TOKEN' in secrets else ''
CODECOV_REPO = secrets['CODECOV_REPO'] if 'CODECOV_REPO' in secrets else 'marco-c/gecko-dev'
ESFRONTLINE = secrets['ESFRONTLINE']
COVERAGE_SERVICE = secrets['COVERAGE_SERVICE'] if 'COVERAGE_SERVICE' in secrets else 'codecov'
ACTIVE_DATA_INDEX = secrets['ACTIVE_DATA_INDEX'] if 'ACTIVE_DATA_INDEX' in secrets else 'coverage'
HG_GIT_MAPPER = secrets['HG_GIT_MAPPER'] if 'HG_GIT_MAPPER' in secrets else 'https://mapper.mozilla-releng.net'
PHABRICATOR_TOKEN = secrets['PHABRICATOR_TOKEN']
