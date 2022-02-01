"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    
    def __init__ (self, start = 0):
        """initialize start at start value."""
        self.start = self.next = start
        
    def __repr__ (self):
        """shows representation of start and next.  next is holding the incremented value start remains at start """
        return f"<SerialGenerator start = {self.start} next={self.next}>"
    
    def generate(self):
        """This will return incremented start value"""
        self.next += 1 
        return self.next
    
    def reset(self):
        """Reset next value back to start original value"""
        self.next = self.start

    