#
# Copyright (c) 2014 QuarksLab.
# This file is part of IRMA project.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License in the top-level directory
# of this distribution and at:
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# No part of the project, including this file, may be copied,
# modified, propagated, or distributed except according to the
# terms contained in the LICENSE file.

import logging

from modules.antivirus.mcafee_vscl import McAfeeVSCL
from probes.antivirus.antivirus import AntivirusProbe

log = logging.getLogger(__name__)


class McAfeeVSCLProbe(AntivirusProbe):

    ##########################################################################
    # plugin metadata
    ##########################################################################

    _plugin_name = "McAfeeVSCL"
    _plugin_version = "0.0.0"
    _plugin_description = ("Antivirus plugin for McAfee " +
                           "VirusScan Command Line (VSCL) scanner")

    ##########################################################################
    # constructor and destructor stuff
    ##########################################################################

    def __init__(self, conf=None, **kwargs):
        # call super classes constructors
        super(McAfeeVSCLProbe, self).__init__(conf, **kwargs)
        self._module = McAfeeVSCL()
