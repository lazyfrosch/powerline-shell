import os
from ..utils import BasicSegment

OS_NAMES = ['OS_PROJECT_NAME', 'OS_TENANT_NAME']

class Segment(BasicSegment):
    def add_to_powerline(self):
        powerline = self.powerline

        for name in OS_NAMES:
            if name in os.environ:
                text = ' %s %s ' % (u'\U00002601', os.environ[name])
                powerline.append(text, 15, 2)
                return
