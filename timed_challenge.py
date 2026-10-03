# Timed Challenge - Question 8: Already Seen
#
# Track a series of user IDs and return the number of new users.
#
# Input: [101, 102, 101, 103, 104, 102]
# Output: 3


def count_new_users(user_ids):
    seen_users = set()
    new_users = 0

    for user_id in user_ids:
        if user_id not in seen_users:
            seen_users.add(user_id)
            new_users += 1

    return new_users


# Tests
print(count_new_users([101, 102, 101, 103, 104, 102]))
print(count_new_users([1, 2, 3, 4]))
print(count_new_users([5, 5, 5, 5]))
print(count_new_users([]))


# Edge case tests
print(count_new_users([100]))
print(count_new_users([1, 2, 1, 2, 3, 3]))

"""
Reflection

For this timed challenge, I chose a set because the problem required me to
track user IDs and determine how many users were new. A set is a good choice
because it only stores unique values and allows fast checking to see if a user
ID has already been seen. This made the solution simple and efficient. The
main operation is checking whether a user ID is in the set, which is O(1) on
average. Adding a new ID to the set is also O(1) on average, so the complete
solution is O(n), where n is the number of user IDs.

The 30-minute time limit affected my decision because I wanted to choose a
solution that I could understand, write, and test quickly. Instead of using a
more complicated structure, I used a set because it directly matches the
problem. I also focused on making the code easy to read and making sure it
worked with different inputs.

Under time pressure, I made the trade-off of choosing a simple and reliable
solution instead of trying to create a more advanced solution. I tested a
normal list, a list with repeated IDs, an empty list, and a list with only one
ID. These tests helped me check that the function worked for different cases.

This challenge showed me that choosing the correct data structure can make a
problem much easier to solve. It also helped me practice making a decision
quickly while thinking about runtime and efficiency.
"""