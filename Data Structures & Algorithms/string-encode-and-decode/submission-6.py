class Solution:

    ret_str = ""
    def encode(self, strs: List[str]) -> str:
        # encode a list of strings to a string
        # "Hello World"
        ret_str = ""
        for i in strs:
            ret_str += i + "`"
        return ret_str

    def decode(self, s: str) -> List[str]:
        # do the opposite
        # "Hello" "World"

        # so the split function doesnt work here... how can i write a manual
        # uncovering. i need to use a delimiter?

        # what is the opposite of this

        ret_str = ""
        ret_str_list = []

        for char in s:
            if char != "`":
                ret_str += char
            else:
                ret_str_list.append(ret_str)
                ret_str = ""
        
        # ret_str_list = s.split()
        return ret_str_list

