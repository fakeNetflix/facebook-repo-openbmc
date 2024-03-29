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

GPIOS = {
    "LC2_DPM_POWER_UP": {
        "uevent": "",
        "direction": "out",
        "active_low": "0",
        "value": "1",
    },
    "LC8_SCD_RESET_L": {
        "uevent": "",
        "direction": "out",
        "active_low": "0",
        "value": "1",
    },
    "BMC_eMMC_RST_N": {
        "uevent": "",
        "edge": "none",
        "direction": "in",
        "active_low": "0",
        "value": "0",
    },
    "LC1_SATELLITE_PROG": {
        "uevent": "",
        "direction": "out",
        "active_low": "0",
        "value": "1",
    },
    "LC4_SATELLITE_PROG": {
        "uevent": "",
        "direction": "out",
        "active_low": "0",
        "value": "1",
    },
    "LC3_STATUS_RED_L": {
        "uevent": "",
        "direction": "out",
        "active_low": "0",
        "value": "1",
    },
    "LC8_SCD_CONFIG_L": {
        "uevent": "",
        "direction": "out",
        "active_low": "0",
        "value": "1",
    },
    "LC5_BAB_SYS_RESET_L": {
        "uevent": "",
        "direction": "out",
        "active_low": "0",
        "value": "1",
    },
    "LC4_SCD_RESET_L": {
        "uevent": "",
        "direction": "out",
        "active_low": "0",
        "value": "1",
    },
    "LC6_BAB_SYS_RESET_L": {
        "uevent": "",
        "direction": "out",
        "active_low": "0",
        "value": "1",
    },
    "LC2_LC_PWR_CYC": {
        "uevent": "",
        "direction": "in",
        "active_low": "0",
        "value": "0",
    },
    "LC8_BAB_SYS_RESET_L": {
        "uevent": "",
        "direction": "out",
        "active_low": "0",
        "value": "1",
    },
    "LC4_LC_PWR_CYC": {
        "uevent": "",
        "direction": "in",
        "active_low": "0",
        "value": "0",
    },
    "LC1_STATUS_RED_L": {
        "uevent": "",
        "direction": "out",
        "active_low": "0",
        "value": "1",
    },
    "BIOS_SEL": {
        "uevent": "",
        "edge": "none",
        "direction": "in",
        "active_low": "0",
        "value": "0",
    },
    "LC3_SATELLITE_PROG": {
        "uevent": "",
        "direction": "out",
        "active_low": "0",
        "value": "1",
    },
    "LC2_BAB_SYS_RESET_L": {
        "uevent": "",
        "direction": "out",
        "active_low": "0",
        "value": "1",
    },
    "LC7_SCD_CONFIG_L": {
        "uevent": "",
        "direction": "out",
        "active_low": "0",
        "value": "1",
    },
    "LC5_FAST_JTAG_EN": {
        "uevent": "",
        "direction": "in",
        "active_low": "0",
        "value": "0",
    },
    "LC2_STATUS_RED_L": {
        "uevent": "",
        "direction": "out",
        "active_low": "0",
        "value": "1",
    },
    "LC3_FAST_JTAG_EN": {
        "uevent": "",
        "direction": "in",
        "active_low": "0",
        "value": "0",
    },
    "TPM_RST_N": {
        "uevent": "",
        "edge": "none",
        "direction": "out",
        "active_low": "0",
        "value": "1",
    },
    "LC2_FAST_JTAG_EN": {
        "uevent": "",
        "direction": "in",
        "active_low": "0",
        "value": "0",
    },
    "LC7_DPM_POWER_UP": {
        "uevent": "",
        "direction": "out",
        "active_low": "0",
        "value": "1",
    },
    "LC2_SCD_RESET_L": {
        "uevent": "",
        "direction": "out",
        "active_low": "0",
        "value": "1",
    },
    "LC1_DPM_POWER_UP": {
        "uevent": "",
        "direction": "out",
        "active_low": "0",
        "value": "1",
    },
    "LC7_FAST_JTAG_EN": {
        "uevent": "",
        "direction": "in",
        "active_low": "0",
        "value": "0",
    },
    "LC5_SATELLITE_PROG": {
        "uevent": "",
        "direction": "out",
        "active_low": "0",
        "value": "1",
    },
    "LC4_SCD_CONFIG_L": {
        "uevent": "",
        "direction": "out",
        "active_low": "0",
        "value": "1",
    },
    "LC8_SATELLITE_PROG": {
        "uevent": "",
        "direction": "out",
        "active_low": "0",
        "value": "1",
    },
    "LC5_DPM_POWER_UP": {
        "uevent": "",
        "direction": "out",
        "active_low": "0",
        "value": "1",
    },
    "LC5_SCD_CONFIG_L": {
        "uevent": "",
        "direction": "out",
        "active_low": "0",
        "value": "1",
    },
    "LC7_SATELLITE_PROG": {
        "uevent": "",
        "direction": "out",
        "active_low": "0",
        "value": "1",
    },
    "LC2_STATUS_GREEN_L": {
        "uevent": "",
        "direction": "out",
        "active_low": "0",
        "value": "0",
    },
    "LC8_STATUS_GREEN_L": {
        "uevent": "",
        "direction": "out",
        "active_low": "0",
        "value": "0",
    },
    "LC8_FAST_JTAG_EN": {
        "uevent": "",
        "direction": "in",
        "active_low": "0",
        "value": "0",
    },
    "LC3_LC_PWR_CYC": {
        "uevent": "",
        "direction": "in",
        "active_low": "0",
        "value": "0",
    },
    "LC2_SATELLITE_PROG": {
        "uevent": "",
        "direction": "out",
        "active_low": "0",
        "value": "1",
    },
    "LC8_LC_PWR_CYC": {
        "uevent": "",
        "direction": "in",
        "active_low": "0",
        "value": "0",
    },
    "LC3_SCD_RESET_L": {
        "uevent": "",
        "direction": "out",
        "active_low": "0",
        "value": "1",
    },
    "LC5_STATUS_GREEN_L": {
        "uevent": "",
        "direction": "out",
        "active_low": "0",
        "value": "0",
    },
    "LC4_STATUS_RED_L": {
        "uevent": "",
        "direction": "out",
        "active_low": "0",
        "value": "1",
    },
    "LC5_SCD_RESET_L": {
        "uevent": "",
        "direction": "out",
        "active_low": "0",
        "value": "1",
    },
    "LC1_SCD_RESET_L": {
        "uevent": "",
        "direction": "out",
        "active_low": "0",
        "value": "1",
    },
    "LC6_DPM_POWER_UP": {
        "uevent": "",
        "direction": "out",
        "active_low": "0",
        "value": "1",
    },
    "LC1_FAST_JTAG_EN": {
        "uevent": "",
        "direction": "in",
        "active_low": "0",
        "value": "0",
    },
    "LC4_BAB_SYS_RESET_L": {
        "uevent": "",
        "direction": "out",
        "active_low": "0",
        "value": "1",
    },
    "LC7_SCD_RESET_L": {
        "uevent": "",
        "direction": "out",
        "active_low": "0",
        "value": "1",
    },
    "LC1_LC_PWR_CYC": {
        "uevent": "",
        "direction": "in",
        "active_low": "0",
        "value": "0",
    },
    "LC8_DPM_POWER_UP": {
        "uevent": "",
        "direction": "out",
        "active_low": "0",
        "value": "1",
    },
    "LC6_LC_PWR_CYC": {
        "uevent": "",
        "direction": "in",
        "active_low": "0",
        "value": "0",
    },
    "LC5_LC_PWR_CYC": {
        "uevent": "",
        "direction": "in",
        "active_low": "0",
        "value": "0",
    },
    "LC2_SCD_CONFIG_L": {
        "uevent": "",
        "direction": "out",
        "active_low": "0",
        "value": "1",
    },
    "LC7_STATUS_RED_L": {
        "uevent": "",
        "direction": "out",
        "active_low": "0",
        "value": "1",
    },
    "LC1_BAB_SYS_RESET_L": {
        "uevent": "",
        "direction": "out",
        "active_low": "0",
        "value": "1",
    },
    "LC6_FAST_JTAG_EN": {
        "uevent": "",
        "direction": "in",
        "active_low": "0",
        "value": "0",
    },
    "LC7_BAB_SYS_RESET_L": {
        "uevent": "",
        "direction": "out",
        "active_low": "0",
        "value": "1",
    },
    "LC6_SCD_RESET_L": {
        "uevent": "",
        "direction": "out",
        "active_low": "0",
        "value": "1",
    },
    "LC4_STATUS_GREEN_L": {
        "uevent": "",
        "direction": "out",
        "active_low": "0",
        "value": "0",
    },
    "TPM_INTR": {
        "uevent": "",
        "edge": "none",
        "direction": "in",
        "active_low": "0",
        "value": "1",
    },
    "LC6_STATUS_RED_L": {
        "uevent": "",
        "direction": "out",
        "active_low": "0",
        "value": "1",
    },
    "LC8_STATUS_RED_L": {
        "uevent": "",
        "direction": "out",
        "active_low": "0",
        "value": "1",
    },
    "LC3_DPM_POWER_UP": {
        "uevent": "",
        "direction": "out",
        "active_low": "0",
        "value": "1",
    },
    "LC7_STATUS_GREEN_L": {
        "uevent": "",
        "direction": "out",
        "active_low": "0",
        "value": "0",
    },
    "LC7_LC_PWR_CYC": {
        "uevent": "",
        "direction": "in",
        "active_low": "0",
        "value": "0",
    },
    "LC6_SATELLITE_PROG": {
        "uevent": "",
        "direction": "out",
        "active_low": "0",
        "value": "1",
    },
    "SUP_PWR_ON": {
        "uevent": "",
        "edge": "none",
        "direction": "in",
        "active_low": "0",
        "value": "0",
    },
    "LC4_FAST_JTAG_EN": {
        "uevent": "",
        "direction": "in",
        "active_low": "0",
        "value": "0",
    },
    "LC3_SCD_CONFIG_L": {
        "uevent": "",
        "direction": "out",
        "active_low": "0",
        "value": "1",
    },
    "LC6_SCD_CONFIG_L": {
        "uevent": "",
        "direction": "out",
        "active_low": "0",
        "value": "1",
    },
    "CPLD_JTAG_SEL_L": {
        "uevent": "",
        "edge": "none",
        "direction": "in",
        "active_low": "0",
        "value": "1",
    },
    "LC1_SCD_CONFIG_L": {
        "uevent": "",
        "direction": "out",
        "active_low": "0",
        "value": "1",
    },
    "LC1_STATUS_GREEN_L": {
        "uevent": "",
        "direction": "out",
        "active_low": "0",
        "value": "0",
    },
    "LC6_STATUS_GREEN_L": {
        "uevent": "",
        "direction": "out",
        "active_low": "0",
        "value": "0",
    },
    "LC3_BAB_SYS_RESET_L": {
        "uevent": "",
        "direction": "out",
        "active_low": "0",
        "value": "1",
    },
    "LC5_STATUS_RED_L": {
        "uevent": "",
        "direction": "out",
        "active_low": "0",
        "value": "1",
    },
    "LC4_DPM_POWER_UP": {
        "uevent": "",
        "direction": "out",
        "active_low": "0",
        "value": "1",
    },
    "LC3_STATUS_GREEN_L": {
        "uevent": "",
        "direction": "out",
        "active_low": "0",
        "value": "0",
    },
}
