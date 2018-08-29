#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import json

data = json.load(open(sys.argv[1]))
print json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True)

