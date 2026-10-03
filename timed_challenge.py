# Pick one question from timed_challenge.txt
# Paste the question as a comment below
# Set a timer for 30 minutes and complete the question!
# 10. Remove by Value
#    Remove the first occurrence of a given value from a sequence.
#    Input: [10, 20, 30, 20], Remove 20
#    Output: [10, 30, 20]

def remove_by_value(sequence, value):
    try:
        index = sequence.index(value)
        return sequence[:index] + sequence[index + 1:]
    except ValueError:
        return sequence[:]