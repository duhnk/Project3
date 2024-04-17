def read_txt_to_list(filename):


  try:
    with open(filename, 'r') as file:
      # Read lines and strip whitespaces
      data_set = [line.strip() for line in file]
      return data_set
  except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
    return []  # Return list

def find_subwords(word, word_set, memo=None):
    if memo is None:
        memo = {}
    if word in memo:  # Check if the result is already computed
        return memo[word]
    
    # Base case: if the word itself is in the set, return it
    if word in word_set:
        memo[word] = {word}
        return {word}
    
    # Initialize the smallest subwords set to an empty set
    smallest_subwords = set()
    # Start with the full word and try to find the smallest subword combination
    for i in range(1, len(word)):
        prefix = word[:i]
        suffix = word[i:]
        
        # If the prefix is a valid word, check the suffix for subwords
        if prefix in word_set:
            suffix_subwords = find_subwords(suffix, word_set, memo)
            # If subwords are found in the suffix, combine them with the prefix
            if suffix_subwords:
                current_subwords = [prefix] + list(suffix_subwords)
                # If this is the first combination found or smaller than the previous one, update the smallest set
                if not smallest_subwords or len(current_subwords) < len(smallest_subwords):
                    smallest_subwords = current_subwords
    
    memo[word] = smallest_subwords  # Store the result in the memo dictionary
    return smallest_subwords

def format_output(input_words, word_set):
    output = []
    for word in input_words:
        subwords = find_subwords(word, word_set)
        if subwords:
            output.append(f"{word} can be split into {len(subwords)} AiW words: {' '.join(subwords)}")
        else:
            output.append(f"{word} cannot be split into AiW words.")
    return '\n'.join(output)

def main():
    import csv
  
    with open('aliceInWonderlandDictionary.csv','r') as inputFile:
        cttData = csv.DictReader(inputFile)
        data=set()
                # Example usage
        filename = "input.txt"
        data_list = read_txt_to_list(filename)

        if data_list:
          print("File loaded:")
        else:
          print("No data found in the file.")
        
        for row in cttData:
            #print(row['names'])
            data.add(row['names'])
            quit()
        formatted_output = format_output(data_list, data)
        print(formatted_output)
        
            
if __name__ == '__main__':
    main()
