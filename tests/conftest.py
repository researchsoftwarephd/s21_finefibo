# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Author: Nuno Fachada

import pytest

@pytest.fixture(scope = 'module')
def return42():
    """Some documentation of our fixture"""
    return 42