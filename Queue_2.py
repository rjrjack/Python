import queue

        # create queue
q = queue.Queue()

        # add elements
q.put(1) # 1
q.put(2) # 2 1
q.put(3) # 3 2 1 

        # now que looks like this:
        # back --> 3 2 1 --> front

        # get and remove first element
first = q.get()
print(first)        # --> 1 
print()
for i in q.queue:
    print(i)
    
print(list(q.queue))