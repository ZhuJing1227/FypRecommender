# ------------------------------------------------------------------
# Copyright (c) 2020 PyInstaller Development Team.
#
# This file is distributed under the terms of the GNU General Public
# License (version 2.0 or later).
#
# The full license is available in LICENSE.GPL.txt, distributed with
# this software.
#
# SPDX-License-Identifier: GPL-2.0-or-later
# ------------------------------------------------------------------

from PyInstaller.utils.hooks import is_module_satisfies, \
    collect_submodules, collect_data_files

tf_pre_1_15_0 = is_module_satisfies("tensorflow < 1.15.0")
tf_post_1_15_0 = is_module_satisfies("tensorflow >= 1.15.0")
tf_pre_2_0_0 = is_module_satisfies("tensorflow < 2.0.0")
tf_pre_2_2_0 = is_module_satisfies("tensorflow < 2.2.0")


# Exclude from data collection:
#  - development headers in include subdirectory
#  - XLA AOT runtime sources
#  - libtensorflow_framework shared library (to avoid duplication)
#  - import library (.lib) files (Windows-only)
data_excludes = [
    "include",
    "xla_aot_runtime_src",
    "libtensorflow_framework.*",
    "**/*.lib",
]

# Under tensorflow 2.3.0 (the most recent version at the time of writing),
# _pywrap_tensorflow_internal extension module ends up duplicated; once
# as an extension, and once as a shared library. In addition to increasing
# program size, this also causes problems on macOS, so we try to prevent
# the extension module "variant" from being picked up.
#
# See pyinstaller/pyinstaller-hooks-contrib#49 for details.
excluded_submodules = ['tensorflow.python._pywrap_tensorflow_internal']


def _submodules_filter(x):
    return x not in excluded_submodules


if tf_pre_1_15_0:
    # 1.14.x and earlier: collect everything from tensorflow
    hiddenimports = collect_submodules('tensorflow',
                                       filter=_submodules_filter)
    datas = collect_data_files('tensorflow', excludes=data_excludes)
elif tf_post_1_15_0 and tf_pre_2_2_0:
    # 1.15.x - 2.1.x: collect everything from tensorflow_core
    hiddenimports = collect_submodules('tensorflow_core',
                                       filter=_submodules_filter)
    datas = collect_data_files('tensorflow_core', excludes=data_excludes)

    # Under 1.15.x, we seem to fail collecting a specific submodule,
    # and need to add it manually...
    if tf_post_1_15_0 and tf_pre_2_0_0:
        hiddenimports += \
            ['tensorflow_core._api.v1.compat.v2.summary.experimental']
else:
    # 2.2.0 and newer: collect everything from tensorflow again
    hiddenimports = collect_submodules('tensorflow',
                                       filter=_submodules_filter)
    datas = collect_data_files('tensorflow', excludes=data_excludes)

    # From 2.6.0 on, we also need to explicitly collect keras (due to
    # lazy mapping of tensorflow.keras.xyz -> keras.xyz)
    if is_module_satisfies("tensorflow >= 2.6.0"):
        hiddenimports += collect_submodules('keras')

excludedimports = excluded_submodules
