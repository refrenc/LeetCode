class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        
        temp_words = [words[0]]
        temp_length = len(words[0])
        for word in words[1:]:
            # 한 줄에 MaxWidth보다 많이 들어오면 정산
            if temp_length + len(word) + 1 > maxWidth:
                # maxWidth - temp_length 만큼 공백 추가
                spaces = maxWidth - temp_length
                while True:
                    if spaces <= 0 or len(temp_words) == 1:
                        break
                    for i in range(len(temp_words)):
                        if spaces > 0 and temp_words[i][0] == " ":
                            temp_words[i] += " "
                            spaces -= 1
                            temp_length += 1
                
                # result에 추가
                result.append(''.join(temp_words) + " " * (maxWidth - temp_length))
                
                # temp_words, temp_length 초기화
                temp_words = [word]
                temp_length = len(word)
                continue
            
            # temp_words, temp_length 갱신
            temp_words += [" ", word]
            temp_length += len(word) + 1
        
        # 마지막 줄 정산
        result.append(''.join(temp_words) + " " * (maxWidth - temp_length))
        
        return result
        