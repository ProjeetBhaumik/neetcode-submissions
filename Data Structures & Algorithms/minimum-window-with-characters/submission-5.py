class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n1 = len(s)
        n2 = len(t)
        if t == "":
            return ""
        count2 = {}
        for c in t:
            count2[c] = count2.get(c,0) + 1
        
        l = 0
        have = 0
        need = len(count2)
        res = [-1,-1]
        resLen = float("infinity")
        window = {}
        for r in range(n1):
            c = s[r]
            window[c] = window.get(c,0) + 1

            if c in count2 and count2[c] == window[c]:
                have += 1

            while have == need:
                if (r-l+1) < resLen:
                    res = [l,r]
                    resLen = r-l+1

                window[s[l]] -= 1
                if s[l] in count2 and window[s[l]]<count2[s[l]]:
                    have -= 1
                l += 1
        i, j = res        
        return s[i:j+1] if resLen != float("infinity") else ""



