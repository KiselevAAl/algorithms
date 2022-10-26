
"""
Код проходится по строке, если в строке находится символ обозначающий драгоценный камень, то прибавляется к счетчику +1

Сложность O(N)
"""

class Solution:
    def numJewelsInStones(jewels, stones):
        count = 0
        for i in stones:                            # цикл для всех камней
            if i in jewels:                        # цикл для поиска драгоценных камней
                count += 1                      # добавляем в счетчик
        return count                                # возвращаем результата


    print(numJewelsInStones('aA', 'aAAbbbb'))

