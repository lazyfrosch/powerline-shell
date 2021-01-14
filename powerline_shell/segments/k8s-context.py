import os
import subprocess
from ..utils import BasicSegment

DEFAULT_CONTEXTS = ['default', 'minikube']
DEFAULT_NS = ['default']


class Segment(BasicSegment):
    def add_to_powerline(self):
        powerline = self.powerline

        try:
            # Check current context
            p = subprocess.Popen(['kubectl', 'config', 'current-context'], stdout=subprocess.PIPE)
            context = p.communicate()[0].decode('utf-8').rstrip()

            # Check current namespace
            ns = ''
            try:
                pns = subprocess.Popen(['kubens', '-c'], stdout=subprocess.PIPE)
                ns = pns.communicate()[0].decode('utf-8').strip()
            except OSError:
                pass

            text = ''

            if context not in DEFAULT_CONTEXTS or ns not in DEFAULT_CONTEXTS:
                text += context

            if ns and ns not in DEFAULT_CONTEXTS:
                text += '/' + ns

            if text != '':
                powerline.append(' 📦 ' + text + ' ', 15, 4)

        except OSError:
            return
