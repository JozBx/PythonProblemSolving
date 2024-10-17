'''
https://www.geeksforgeeks.org/given-a-sequence-of-words-print-all-anagrams-together/
Following is another method to print all anagrams together. 
Take two auxiliary arrays, index array, and word array. Populate the word array with the given sequence of words. 
Sort each individual word of the word array. Finally, sort the word array and keep track of the corresponding indices. 
After sorting, all the anagrams cluster together. Use the index array to print the strings from the original array of strings.
'''

from typing import Union

def get_all_anagrams(array: Union[list, tuple]) -> list:
    '''This function takes an array and returns all anagrams grouped together.'''
    
    # Raise an error if the array is not of type list/tuple or if the values are not strings
    if isinstance(array, (list, tuple)) is False:
        raise TypeError("The array must be of type list or tuple")  
    elif all(isinstance(x, str) for x in array) is False:
        raise TypeError("All values of the array must be strings")

    length_array = len(array)  # Get the length of the array

    # Copy the indices and words into two arrays
    index = []
    words = []
    for i in range(length_array):
        index.append(i)  # Add index into array
        words.append(array[i])  # Add corresponding word into array

    # Sort individual words in the words array
    sorted_words = ["".join(sorted(word)) for word in words]

    # Group together the original index and the sorted words, and sort that new list by the sorted words
    indexed_sorted_words = sorted(zip(index, sorted_words), key=lambda x: x[1])

    # Gather the original words from the array, in the order of their sorted anagram groups
    result = [array[i] for i, _ in indexed_sorted_words]

    return result

# Test the function
arr = ["cat", "dog", "tac", "god", "act"]
anagrams = get_all_anagrams(arr)
print(f"The list of anagrams for the given list {arr} is: {anagrams}")