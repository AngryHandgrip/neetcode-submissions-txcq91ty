class Solution:

    def encode(self, strs: List[str]) -> str:
        enc_str = ''
        for s in strs:
            enc_str += f'{len(s)}#{s}'
        return enc_str
    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            len_del = int(s[i:j])
            strs.append(s[j+1:j+len_del+1])
            i = len_del + j + 1
        return strs