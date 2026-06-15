class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            encoded_string += f"{len(s)}."
            encoded_string += s
        return encoded_string

    def decode(self, s: str) -> List[str]:
        if s == "0.":
            return [""]
        current_word_length_str = ""
        begin = True
        strs = []
        for char in s:
            if begin:
                current_word = ""
                if char.isdigit():
                    current_word_length_str += char
                if char == ".":
                    current_word_length = int(current_word_length_str)
                    begin = False
            else:
                current_word += char
                current_word_length -= 1
                if current_word_length == 0:
                    begin = True
                    strs.append(current_word)
                    current_word_length_str = ""

        return strs

            


