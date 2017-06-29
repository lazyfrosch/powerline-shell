import subprocess
import re

def add_rvm_segment():
    try:
        version = ''

        if os.environ.has_key("RUBY_VERSION"):
          version += os.environ["RUBY_VERSION"]

        if os.environ.has_key("GEM_HOME"):
          match = re.search('@(\w+)$', os.environ["GEM_HOME"])
          if match:
            version += '@' + match.group(1)

        if version:
          powerline.append(" "+version+" ", 0, 45)
    except OSError:
        return

add_rvm_segment()
