class Solution:
    def capitalizeTitle(self, title: str) -> str:
        words = title.split()

        new_list = []

        for word in words:
            if len(word) > 2:
                new_word = word[0].upper() + word[1:].lower()
                new_list.append(new_word)
            else:
                new_list.append(word.lower())
        return ' '.join(new_list)


        
