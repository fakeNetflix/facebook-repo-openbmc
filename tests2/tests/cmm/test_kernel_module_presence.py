#!/usr/bin/env python
#
# Copyright 2018-present Facebook. All Rights Reserved.
#
# This program file is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation; version 2 of the License.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
# for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program in a file named COPYING; if not, write to the
# Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA
#
import unittest

from common.base_kernel_module_presence_test import BaseKernelModulePresenceTest


class KernelModulePresenceTest(BaseKernelModulePresenceTest, unittest.TestCase):
    def set_kmods(self):
        self.expected_kmod = [
            "gpio_pca953x",
            "pfe3000",
            "fancpld",
            "cmmcpld",
            "i2c_dev_sysfs",
            "i2c_mux_pca954x",
            "ext4",
            "mbcache",
            "jbd2",
            "crypto_hash",
        ]
