import re

import pynvim


@pynvim.plugin
class TestPlugin(object):
    def __init__(self, nvim):
        self.nvim = nvim

    @pynvim.function("LintSplunk")
    def lintSplunk(self, args):
        current_line = self.nvim.current.line
        front = current_line.split("(")
        i = 0
        j = 0
        res = ""
        for line in front:
            p = ""
            if j != 0:
                p = "("
            back = re.findall("\)", line)
            line = ((i) * "\t") + p + line
            self.nvim.current.buffer.append(line, -1)
            if len(back) == 0:
                i = i + 1
            elif len(back) > 1:
                i = i - len(back)
                if i < 0:
                    i = 0
            j = j + 1
        self.nvim.current.line = ""
        return
