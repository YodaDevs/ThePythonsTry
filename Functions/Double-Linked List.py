# Double-Linked List
#
# The head of the list always 'points' to the first Node
# The tail of the list always 'points' to the last Node
#

class No(object):
 
    def __init__(self, data, previousNode, nextNode):
        self.data = data
        self.previousNode = previousNode
        self.nextNode = nextNode
 
 
class DoubleLinkedList(object):
 
    head = None
    tail = None
 
    def add(self, data):
        """ Adds a new one to the list. """
        # Creates a new one by pointing to None (previous and next)
        new_no = No(data, None, None)

        # If the head is None the list is empty
        # Both the head and the tail receive the new Node
        if self.head is None:
            self.head = new_no
            self.tail = new_no
        # Otherwise, if there is already any value in the list
        else:
            # The previous 'points' to the tail (last in not added)
            new_no.previousNode = self.tail
            # The next always points to None
            new_no.nextNode = None
            # Next to the tail always points to the new Node
            self.tail.nextNode = new_no
            # The tail is now the new Node
            self.tail = new_no
 
    def delete(self, data):
        """ Removes an from the list. """
        # The current Node is the first Node in the list
        no_current = self.head
 
        # Let's look for the data we want to remove 
        # As long as the current Node is valid
        while no_current is not None:
            # 
            if no_current.data == data:
                # If the data we are looking for this Node first Node
                # From the list, we do not have previous
                if no_current.previousNode is None:
                    # The head 'points' to the next Node in the list
                    self.head = no_current.nextNode
                    # And the previous one from the next Node points to None
                    no_current.nextNode.previousNode = None
                else:
                    # Example: Removing the value 5
                    # ... <---> | 2 | <---> | 5 | <---> | 12 | <---> ...
                    #
                    # The next of 2 will point to 12 and
                    # The previous one of value 12 points to 2
                    #                     ---------------
                    # ... <---> | 2 | <---|--- | 5 | ---|---> | 12 | <---> ... 
                    no_current.previousNode.nextNode = no_current.nextNode
                    no_current.nextNode.previousNode = no_current.previousNode

            # If it is not the Node we are looking for go to the next one
            no_current = no_current.nextNode
 
    def print_linked_list(self):
        """ Shows all the data in the list. """
        print "Double-Linked List:"

        # The current Node is the first Node in the list
        no_current = self.head

        no = ""
        # For each valid Node in the list
        while no_current is not None:
            if no_current.previousNode is None:
                no += "None "
            no += "<---> | " + str(no_current.data) + " | "
            if no_current.nextNode is None:
                no += "<---> None"
 
            no_current = no_current.nextNode
        print no
        print "="*80
 
