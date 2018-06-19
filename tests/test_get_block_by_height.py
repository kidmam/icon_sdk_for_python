#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2018 theloop Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest, json
from icx.wallet import Wallet
from icx.utils import validate_block


class TestGetBlockByHeight(unittest.TestCase):

    def test0(self):
        """ Case to get block by Height successfully
        """
        # Given, When
        block = Wallet.get_block_by_height(10)

        # Then
        self.assertTrue(validate_block(block))


