Statement : Return the number (count) of vowels in the given string. 
Input : A string either containing containing vowel or not.
        2) Can be empty string.
        3) Vowels passed are only in lowercase.
Output : Integer count of occurences of vowels in the string.

Code : 
      def get_count(input_str):
        num_vowels = 0
        for i in input_str:
                if i in "aeiou":
                    num_vowels += 1
        return num_vowels
