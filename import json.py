from base64 import decode
import json
import pip._vendor.requests

response= pip._vendor.requests.get("https://jsonplaceholder.typicode.com/todos")
todos= json.loads(response.text)

#print(todos[:2])


#Figure out which users have the most todo items
# user_ids & number of completed todos for that user
#key: user_id
#value: counter of how many completed as true

#if it exists set counter +=1
#if it doesn't exist we are gonna have to add the user_id = 1

todos_by_user= {}

for todo in todos:
    if todo["completed"]:
        #check if the todo and we wanna capture the userid 
        #increment the existing users counte
        ###if the user hasn't been seen in the todos_by_user {} set their count to 1
        if todo["userId"] not in todos_by_user:
            todos_by_user[todo["userId"]] = 1
        else:
            todos_by_user[todo["userId"]] += 1


#print(todos_by_user)

# Create a sorted list of (userId, num_complete) pairs. **tuple
top_users= sorted(todos_by_user.items(), key=lambda x: x[1], reverse=True)

#print(top_users)

# Get the maximum number of complete TODOs.
max_todos = max(todos_by_user.values())
#print(max_todos)

# Create a list of all users who have completed the maximum number of TODOs.
users= []
for user, num_complete in top_users:
    if num_complete == max_todos:
        users.append(str(user))

#print(users)


# All of the completed Todos, for the users that have (the maximum number)12 tododos completed

# Define a function to filter out completed TODOs 
# of users with max completed TODOS.
def keep(todo):
    is_complete = todo["completed"]
    has_max_count = str(todo["userId"]) in users
    return is_complete and has_max_count

# Write filtered TODOs to file.
with open("filtered_data_file.json", "w") as data_file:
    filtered_todos = list(filter(keep, todos))
    json.dump(filtered_todos, data_file, indent=4)