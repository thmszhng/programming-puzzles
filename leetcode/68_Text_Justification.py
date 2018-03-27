class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        lines = []
        
        # break words into lines
        line = []
        line_width = 0
        for word in words:
            if line_width + len(word) > maxWidth - len(line):
                lines.append(line)
                line = []
                line_width = 0
            line.append(word)
            line_width += len(word)
        lines.append(line)
        
        # add spaces to lines
        for i in range(len(lines) - 1):
            line = lines[i]
            for j in range(maxWidth - sum(map(len, line))):
                line[(j % (len(line) - 1)) if len(line) > 1 else 0] += ' '
            lines[i] = ''.join(line)
        lines[-1] = ' '.join(lines[-1]) + ' '*(maxWidth - sum(map(len, lines[-1])) - len(lines[-1]) + 1)
        
        return lines
